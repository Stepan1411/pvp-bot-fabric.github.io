# 🤖 ПВП-бот — Wiki

Добро пожаловать в официальную документацию PVP-бота!

---

## 📖 About

PVP Bot is a Minecraft Fabric mod that adds intelligent combat bots powered by HeroBot mod. Create armies of bots, organize them into factions, and watch epic battles unfold!

---

## 🚀 Быстрый старт

1. Установите [Fabric Loader](https://fabricmc.net/) и [HeroBot Mod](https://modrinth.com/mod/herobot).
2. Загрузите PVP Bot и поместите его в свой`mods`папка
3. Запустите игру и используйте`/pvpbot spawn BotName`чтобы создать своего первого бота!

---

## 📚 Documentation

| Страница | Описание |
|------|-------------|
| [🎮 Команды](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Commands) | Все доступные команды |
| [⚔️ Боевая система](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Combat) | Как боты дерутся |
| [💥 Взрывной бой](https://github.com/Stepan1411/pvp-bot-fabric/wiki/ExplosiveCombat) | Кристалл PVP и Якорь PVP |
| [🚀 ElytraMace](https://github.com/Stepan1411/pvp-bot-fabric/wiki/ElytraMace) | Передовая техника воздушного боя |
| [🚶 Навигация](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Navigation) | Базовый поиск пути |
| [🏃Движение](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Movement) | Следовать, сопровождать и переходить по командам |
| [🛤️ Пути](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Paths) | Система путей и путевые точки |
| [👥 Фракции](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Factions) | Командная система |
| [🎒 Комплекты](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Kits) | Пресеты оборудования |
| [⚙️ Настройки](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Settings) | Все варианты конфигурации |

---

## 💡 Быстрые примеры

### Создайте простого бота
```
/pvpbot spawn MyBot
```

### Включить Кристальное PVP
```
/pvpbot settings crystalpvp true
```

### Включить трюк ElytraMace
```
/pvpbot settings elytramace true
```

### Заставить бота следовать за игроком
```
/pvpbot follow Bot1 Steve
```

### Сделать бота сопровождающим (следовать + защищать) игрока
```
/pvpbot escort Bot1 Steve
```

### Заставьте две команды сражаться
```
/pvpbot spawn Red1
/pvpbot spawn Blue1
/pvpbot faction create Red
/pvpbot faction create Blue
/pvpbot faction add Red Red1
/pvpbot faction add Blue Blue1
/pvpbot faction hostile Red Blue
```

---

## 🔗 Ссылки

- [Репозиторий GitHub](https://github.com/Stepan1411/pvp-bot-fabric)
- [Страница Модринта](https://modrinth.com/mod/pvp-bot)
- [Bug Reports](https://github.com/Stepan1411/pvp-bot-fabric/issues)
