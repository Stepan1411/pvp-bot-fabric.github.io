import { defineConfig } from 'vitepress'
import { fileURLToPath } from 'url'
import { readFileSync, existsSync } from 'fs'
import { resolve, dirname } from 'path'

const __filename = fileURLToPath(import.meta.url)
const __dirname = dirname(__filename)
const root = resolve(__dirname, '..')
const wikiDir = resolve(root, 'wiki')

function loadPages(path) {
  try {
    return JSON.parse(readFileSync(resolve(wikiDir, path), 'utf-8')).pages
  } catch {
    return []
  }
}

function slugify(id) {
  return id
    .replace(/([a-z])([A-Z])/g, '$1-$2')
    .replace(/([A-Z]+)([A-Z][a-z])/g, '$1-$2')
    .toLowerCase()
}

function normalizeId(id) {
  return id.toLowerCase()
}

const playerPages = loadPages('pages.json')
const devPages = loadPages('dev_pages.json')

const navEn = [
  { text: 'Home', link: '/' },
  { text: 'Guide', link: '/guide/' },
  { text: 'Developers', link: '/dev/' },
]

const navRu = [
  { text: 'Главная', link: '/ru/' },
  { text: 'Руководство', link: '/ru/guide/' },
]

const navDe = [
  { text: 'Startseite', link: '/de/' },
  { text: 'Anleitung', link: '/de/guide/' },
]

const navFr = [
  { text: 'Accueil', link: '/fr/' },
  { text: 'Guide', link: '/fr/guide/' },
]

const navEs = [
  { text: 'Inicio', link: '/es/' },
  { text: 'Guía', link: '/es/guide/' },
]

const navZh = [
  { text: '主页', link: '/zh/' },
  { text: '指南', link: '/zh/guide/' },
]

const localesConfig = {
  root: { label: 'English', lang: 'en-US', themeConfig: { nav: navEn } },
  ru: { label: 'Русский', lang: 'ru-RU', themeConfig: { nav: navRu } },
  de: { label: 'Deutsch', lang: 'de-DE', themeConfig: { nav: navDe } },
  fr: { label: 'Français', lang: 'fr-FR', themeConfig: { nav: navFr } },
  es: { label: 'Español', lang: 'es-ES', themeConfig: { nav: navEs } },
  zh: { label: '简体中文', lang: 'zh-CN', themeConfig: { nav: navZh } },
}

const localeToDir = {
  ru: 'ru',
  de: 'de',
  fr: 'fr',
  es: 'es',
  zh: 'zh-CN',
}

function getTranslationKey(locale) {
  return locale === 'root' ? 'en' : locale
}

function linkFor(locale, prefix, id) {
  const base = locale === 'root' ? '/' : `/${locale}/`
  const isHome = prefix === 'guide' ? normalizeId(id) === 'home' : slugify(id) === 'home'
  return isHome ? `${base}${prefix}/` : `${base}${prefix}/${normalizeId(id)}`
}

function getSidebarPages(locale, pages, prefix) {
  const translationKey = getTranslationKey(locale)
  return pages.map(p => ({
    text: p.translations?.[translationKey] || p.translations?.en || p.id,
    link: linkFor(locale, prefix, p.id),
  }))
}

const sidebar = {}
for (const locale of Object.keys(localesConfig)) {
  sidebar[`/${locale === 'root' ? '' : locale + '/'}guide/`] = [
    { text: 'Guide', items: getSidebarPages(locale, playerPages, 'guide') },
  ]
  if (locale === 'root') {
    sidebar[`/dev/`] = [
      { text: 'Developers', items: getSidebarPages(locale, devPages, 'dev') },
    ]
  }
}

const rewrites = {}
for (const locale of Object.keys(localesConfig)) {
  const dir = localeToDir[locale]
  const prefix = locale === 'root' ? '' : `${locale}/`
  const sourcePrefix = dir ? `${dir}/` : ''

  for (const p of playerPages) {
    const src = dir
      ? `translates/${dir}/player/${p.file}`
      : `wiki/player/${p.file}`
    if (dir && !existsSync(resolve(root, 'translates', dir, 'player', p.file))) continue
    const dest = normalizeId(p.id) === 'home'
      ? `${prefix}guide/index.md`
      : `${prefix}guide/${normalizeId(p.id)}.md`
    rewrites[src] = dest
  }

  if (locale === 'root') {
    for (const p of devPages) {
      const src = `wiki/developer/${p.file}`
      const dest = slugify(p.id) === 'home'
        ? `dev/index.md`
        : `dev/${slugify(p.id)}.md`
      rewrites[src] = dest
    }
  }
}

export default defineConfig({
  title: 'PVP Bot',
  description: 'Advanced Minecraft Fabric mod that adds AI bots for PvP',
  lang: 'en-US',
  base: '/',

  locales: localesConfig,

  srcExclude: [
    'pvp-bot-fabric/**',
    'wiki/player/en/**',
    'wiki/developer/en/**',
    'translates/**/.*',
  ],

  rewrites,

  ignoreDeadLinks: true,

  head: [
    ['link', { rel: 'icon', href: '/images/favicon.png' }],
  ],

  themeConfig: {
    logo: '/images/logo.png',

    sidebar,

    socialLinks: [
      { icon: 'github', link: 'https://github.com/Stepan1411/pvp-bot-fabric' },
    ],

    footer: {
      message: 'PVP Bot Fabric — Open source Minecraft mod',
      copyright: '© Stepan1411',
    },
  },
})
