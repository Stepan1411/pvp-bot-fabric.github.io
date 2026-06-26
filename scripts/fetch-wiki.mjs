import { writeFileSync, readFileSync, mkdirSync } from 'fs'
import { resolve, dirname } from 'path'
import { fileURLToPath } from 'url'

const __filename = fileURLToPath(import.meta.url)
const __dirname = dirname(__filename)
const root = resolve(__dirname, '..')

const pagesBase = 'https://stepan1411.github.io/pvp-bot-fabric/wiki'
const mdBase = 'https://stepan1411.github.io/pvp-bot-fabric/wiki'
const cache = resolve(root, 'wiki')

async function fetchText(url) {
  const res = await fetch(url)
  if (!res.ok) throw new Error(`Failed to fetch ${url}: ${res.status}`)
  return res.text()
}

function fixHtmlTags(content) {
  const lines = content.split('\n')
  let inCode = false
  const result = []
  for (const line of lines) {
    if (line.trimStart().startsWith('```')) { inCode = !inCode; result.push(line); continue }
    if (!inCode) {
      if (line.includes('<String>') && !line.trim().startsWith('**Returns:**')) {
        result.push(line)
      } else if (/<[A-Z][a-zA-Z]*>/.test(line)) {
        result.push(line.replace(/<([A-Z][a-zA-Z]*)>/g, '`<$1>`'))
      } else {
        result.push(line)
      }
    } else {
      result.push(line)
    }
  }
  return result.join('\n')
}

async function download(url, dest) {
  let content
  try {
    content = await fetchText(url)
  } catch {
    try {
      content = readFileSync(dest, 'utf-8')
      console.log(`  ⚡ ${url.split('/').pop()} (cached)`)
      return
    } catch {
      throw new Error(`Failed to fetch ${url}: missing from remote and no cached copy`)
    }
  }
  content = fixHtmlTags(content)
  mkdirSync(dirname(dest), { recursive: true })
  writeFileSync(dest, content, 'utf-8')
  console.log(`  ✓ ${url.split('/').pop()}`)
}

async function main() {
  console.log('Fetching wiki from', mdBase)

  const pagesUrl = `${pagesBase}/pages.json`
  const devPagesUrl = `${pagesBase}/dev_pages.json`

  const pagesJson = JSON.parse(await fetchText(pagesUrl))
  const devPagesJson = JSON.parse(await fetchText(devPagesUrl))

  mkdirSync(cache, { recursive: true })

  const extraPages = [
    { id: 'ExplosiveCombat', icon: '💥', file: 'ExplosiveCombat.md', translations: { en: 'Explosive Combat', ru: 'Взрывной бой', zh: '爆炸战斗', fr: 'Combat explosif', es: 'Combate explosivo', de: 'Explosiver Kampf' } },
    { id: 'Movement', icon: '🚶', file: 'Movement.md', translations: { en: 'Movement', ru: 'Передвижение', zh: '移动', fr: 'Mouvement', es: 'Movimiento', de: 'Bewegung' } },
    { id: 'ElytraMace', icon: '🪽', file: 'ElytraMace.md', translations: { en: 'Elytra Mace', ru: 'Elytra Mace', zh: '鞘翅锤', fr: 'Elytra Mace', es: 'Elytra Mace', de: 'Elytra Mace' } },
  ]
  for (const ep of extraPages) {
    if (!pagesJson.pages.find(p => p.id === ep.id)) pagesJson.pages.push(ep)
  }

  writeFileSync(resolve(cache, 'pages.json'), JSON.stringify(pagesJson, null, 2), 'utf-8')
  writeFileSync(resolve(cache, 'dev_pages.json'), JSON.stringify(devPagesJson, null, 2), 'utf-8')
  console.log('  ✓ pages.json')
  console.log('  ✓ dev_pages.json')

  for (const p of pagesJson.pages) {
    await download(`${mdBase}/player/${p.file}`, resolve(cache, 'player', p.file))
  }

  for (const p of devPagesJson.pages) {
    await download(`${mdBase}/developer/${p.file}`, resolve(cache, 'developer', p.file))
  }

  console.log(`Done — ${pagesJson.pages.length + devPagesJson.pages.length + 2} files`)
}

main().catch(err => {
  console.error('Fetch failed:', err.message)
  process.exit(1)
})
