#!/usr/bin/env python3
"""
Wiki Translation Script
Translates all .md files from source directory to multiple languages
"""

import os
import sys
from pathlib import Path
from deep_translator import GoogleTranslator
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import threading
import logging
import queue

# Setup logging
logging.basicConfig(
    filename='translation_errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Configuration
SOURCE_DIR = "."  # Current directory (where script is located)
OUTPUT_DIR = "."  # Output in current directory
SOURCE_LANG = "en"  # Source language
TARGET_LANGUAGES = ["ru", "zh-CN", "fr", "es", "de"]  # Target languages
MAX_WORKERS = 32  # Number of parallel translations

# Global progress bars dictionary and worker queue
progress_bars = {}
pbar_lock = threading.Lock()
worker_queue = queue.Queue()

# Initialize worker queue
for i in range(MAX_WORKERS):
    worker_queue.put(i)

def translate_text(text, target_lang, source_lang=SOURCE_LANG):
    """Translate text to target language"""
    try:
        # Skip empty text
        if not text or not text.strip():
            return text if text else ""
        
        # Limit text length to avoid API errors
        if len(text) > 5000:
            # Split into chunks
            chunks = [text[i:i+4000] for i in range(0, len(text), 4000)]
            translated_chunks = []
            for chunk in chunks:
                if not chunk.strip():
                    translated_chunks.append(chunk)
                    continue
                try:
                    translator = GoogleTranslator(source=source_lang, target=target_lang)
                    result = translator.translate(chunk)
                    translated_chunks.append(result if result else chunk)
                    time.sleep(0.1)
                except Exception as e:
                    logging.error(f"Chunk translation error: {e}")
                    translated_chunks.append(chunk)
            return ' '.join(translated_chunks)
        
        translator = GoogleTranslator(source=source_lang, target=target_lang)
        result = translator.translate(text)
        
        # Ensure we always return a string
        if result is None:
            logging.warning(f"Translation returned None for: {text[:50]}...")
            return text
        
        return result
    except Exception as e:
        error_msg = f"Error translating to {target_lang}: {e} | Text: {text[:100] if text else 'None'}..."
        logging.error(error_msg)
        return text if text else ""  # Return original text or empty string on error

def translate_markdown_file(file_path, target_lang, worker_id):
    """Translate a markdown file while preserving formatting"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split content into lines
    lines = content.split('\n')
    translated_lines = []
    
    in_code_block = False
    total_lines = len(lines)
    
    # Get or create progress bar for this worker
    with pbar_lock:
        if worker_id not in progress_bars:
            progress_bars[worker_id] = tqdm(
                total=total_lines,
                desc=f"Worker {worker_id:2d}",
                position=worker_id + 1,
                leave=True,
                bar_format='{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]'
            )
        else:
            progress_bars[worker_id].reset(total=total_lines)
        
        pbar = progress_bars[worker_id]
        pbar.set_description(f"Worker {worker_id:2d}: {file_path.name[:15]:15s} → {target_lang}")
    
    for idx, line in enumerate(lines):
        # Update progress bar
        pbar.update(1)
        
        # Check if we're entering/exiting a code block
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            translated_lines.append(line)
            continue
        
        # Don't translate code blocks
        if in_code_block:
            translated_lines.append(line)
            continue
        
        # Don't translate empty lines
        if not line.strip():
            translated_lines.append(line)
            continue
        
        # Don't translate inline code (between backticks)
        if '`' in line:
            # Split by backticks and translate only non-code parts
            parts = line.split('`')
            translated_parts = []
            for i, part in enumerate(parts):
                if i % 2 == 0:  # Not inside backticks
                    if part.strip():
                        translated = translate_text(part, target_lang)
                        # Ensure we got a valid translation
                        translated_parts.append(translated if translated else part)
                    else:
                        translated_parts.append(part)
                else:  # Inside backticks (code)
                    translated_parts.append(part)
            translated_lines.append('`'.join(translated_parts))
        else:
            # Translate the line
            translated = translate_text(line, target_lang)
            # Ensure we got a valid translation
            translated_lines.append(translated if translated else line)
        
        # Small delay to avoid rate limiting
        time.sleep(0.02)
    
    return '\n'.join(translated_lines)

def translate_file_task(md_file, lang, output_path):
    """Task for translating a single file to a single language"""
    # Get worker ID from queue
    worker_id = worker_queue.get()
    
    try:
        lang_dir = output_path / lang
        lang_dir.mkdir(parents=True, exist_ok=True)
        
        translated_content = translate_markdown_file(md_file, lang, worker_id)
        
        output_file = lang_dir / md_file.name
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(translated_content)
        
        # Mark worker as done
        with pbar_lock:
            if worker_id in progress_bars:
                progress_bars[worker_id].set_description(f"Worker {worker_id:2d}: Idle")
                progress_bars[worker_id].reset(total=100)
                progress_bars[worker_id].refresh()
        
        return (md_file.name, lang, True, None)
    except Exception as e:
        error_msg = f"Error in {md_file.name} → {lang}: {str(e)}"
        logging.error(error_msg)
        
        with pbar_lock:
            if worker_id in progress_bars:
                progress_bars[worker_id].set_description(f"Worker {worker_id:2d}: ✗ Error")
                progress_bars[worker_id].refresh()
        
        return (md_file.name, lang, False, str(e))
    finally:
        # Return worker ID to queue
        worker_queue.put(worker_id)

def main():
    """Main function"""
    print("Wiki Translation Script")
    print("=" * 50)
    
    # Get script directory
    script_dir = Path(__file__).parent
    source_path = script_dir / SOURCE_DIR
    
    # Get all .md files (excluding this script's directory subfolders)
    md_files = [f for f in source_path.glob("*.md")]
    
    if not md_files:
        print(f"No .md files found in current directory")
        print(f"Looking in: {source_path.absolute()}")
        sys.exit(1)
    
    print(f"Found {len(md_files)} markdown files")
    print(f"Target languages: {', '.join(TARGET_LANGUAGES)}")
    print()
    
    # Create output directories in script directory
    output_path = script_dir / OUTPUT_DIR
    
    # Copy source files to en directory
    en_dir = output_path / SOURCE_LANG
    en_dir.mkdir(parents=True, exist_ok=True)
    
    for md_file in md_files:
        # Copy original to en directory
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        en_file = en_dir / md_file.name
        with open(en_file, 'w', encoding='utf-8') as f:
            f.write(content)
    
    print(f"✓ Copied {len(md_files)} files to {SOURCE_LANG}/")
    print()
    
    # Create translation tasks
    tasks = []
    for md_file in md_files:
        for lang in TARGET_LANGUAGES:
            tasks.append((md_file, lang, output_path))
    
    total_tasks = len(tasks)
    print(f"Starting translation of {total_tasks} tasks ({len(md_files)} files × {len(TARGET_LANGUAGES)} languages)")
    print(f"Using {MAX_WORKERS} parallel workers")
    print()
    
    # Create main progress bar
    main_pbar = tqdm(
        total=total_tasks,
        desc="Overall",
        position=0,
        leave=True,
        bar_format='{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}] {postfix}'
    )
    
    # Initialize worker progress bars
    for i in range(MAX_WORKERS):
        progress_bars[i] = tqdm(
            total=100,
            desc=f"Worker {i:2d}: Idle",
            position=i + 1,
            leave=True,
            bar_format='{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt}'
        )
    
    # Execute translations in parallel
    results = {'success': 0, 'failed': 0}
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # Submit all tasks
        future_to_task = {
            executor.submit(translate_file_task, md_file, lang, output_path): (md_file.name, lang)
            for md_file, lang, output_path in tasks
        }
        
        # Process results as they complete
        for future in as_completed(future_to_task):
            file_name, lang = future_to_task[future]
            try:
                result_file, result_lang, success, error = future.result()
                
                if success:
                    results['success'] += 1
                    main_pbar.set_postfix_str(f"✓ {result_file} → {result_lang}")
                else:
                    results['failed'] += 1
                    main_pbar.set_postfix_str(f"✗ {result_file} → {result_lang}")
                
                main_pbar.update(1)
            except Exception as e:
                results['failed'] += 1
                logging.error(f"Task execution error for {file_name} → {lang}: {e}")
                main_pbar.update(1)
    
    # Close all progress bars
    main_pbar.close()
    for pbar in progress_bars.values():
        pbar.close()
    
    print()
    print("=" * 50)
    print("Translation complete!")
    print(f"✓ Success: {results['success']}/{total_tasks}")
    if results['failed'] > 0:
        print(f"✗ Failed: {results['failed']}/{total_tasks}")
        print(f"⚠️  Check 'translation_errors.log' for details")
    print()
    print(f"Output directory: {output_path.absolute()}")
    print()
    print("Created folders:")
    for lang in [SOURCE_LANG] + TARGET_LANGUAGES:
        lang_dir = output_path / lang
        if lang_dir.exists():
            file_count = len(list(lang_dir.glob("*.md")))
            print(f"  {lang}/ - {file_count} files")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nTranslation interrupted by user")
        sys.exit(0)
