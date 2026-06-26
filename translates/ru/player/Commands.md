# 🎮 Команды

Все команды PVP-бота начинаются с`/pvpbot`. Требуется уровень разрешений 2 (оператор).

---

## 📋 Table of Contents

- [Управление ботами](#-bot-management)
- [Боевые команды](#-боевые-команды)
- [Faction Commands](#-faction-commands)
- [Команды набора](#-kit-commands)
- [Команды пути](#-команды пути)
- [Настройки](#-настройки)

---

## 🤖 Управление ботами

| Команда | Описание |
|---------|-------------|
| `/pvpbot spawn [name]`| Создать нового бота (случайное имя, если не указано) |
| `/pvpbot massspawn <count>`| Создавать несколько ботов со случайными именами (1-50) |
| `/pvpbot remove <name>`| Удалить бота |
| `/pvpbot removeall`| Удалить всех ботов |
| `/pvpbot list`| Список всех активных ботов |
| `/pvpbot menu`| Открыть меню графического интерфейса |
| `/pvpbot inventory <name>`| Показать инвентарь бота |

### Примеры

```mcfunction
# Create a bot with random name
/pvpbot spawn

# Create a bot named "Guard1"
/pvpbot spawn Guard1

# Spawn 10 bots with random names (10% chance for special names)
/pvpbot massspawn 10

# Remove the bot
/pvpbot remove Guard1

# See all bots
/pvpbot list
```

**Примечание.** При создании ботов со случайными именами существует 10 % вероятность того, что они получат особое имя (`nantag`или`Stepan1411`) вместо сгенерированного имени.

---

## ⚔️ Боевые команды

| Команда | Описание |
|---------|-------------|
| `/pvpbot attack <bot> <target>`| Приказать боту атаковать игрока/сущность |
| `/pvpbot stop <bot>`| Не дать боту атаковать |
| `/pvpbot target <bot>` | Show bot's current target |

---

## 🚶 Команды движения

| Command | Description |
|---------|-------------|
| `/pvpbot follow <bot> <target>` | Make bot follow a player/bot |
| `/pvpbot escort <bot> <target>` | Make bot follow and protect a target |
| `/pvpbot goto <bot> <x> <y> <z>`| Переместить бота в определенные координаты |
| `/pvpbot stopmovement <bot>` | Stop bot movement |

### Примеры движений

```mcfunction
# Make Bot1 follow player Steve
/pvpbot follow Bot1 Steve

# Make Bot2 escort (follow + protect) player Alex
/pvpbot escort Bot2 Alex

# Send Bot3 to coordinates 100 64 200
/pvpbot goto Bot3 100 64 200

# Stop Bot1 from moving
/pvpbot stopmovement Bot1
```

**Примечание:**
- **Следовать**: бот поддерживает расстояние в 3 блока от цели.
- **Сопровождение**: то же самое, что и ниже, но бот будет защищать цель в случае нападения.
- **Goto**: бот перемещается к координатам, используя интеллектуальный поиск пути (баритон, если включен).

### Примеры

```mcfunction
# Make Bot1 attack player Steve
/pvpbot attack Bot1 Steve

# Stop the attack
/pvpbot stop Bot1

# Check who Bot1 is targeting
/pvpbot target Bot1
```

---

## 👥 Команды фракций

| Команда | Описание |
|---------|-------------|
| `/pvpbot faction create <name>`| Создать новую фракцию |
| `/pvpbot faction delete <name>`| Удалить фракцию |
| `/pvpbot faction add <faction> <player>`| Добавить игрока/бота во фракцию |
| `/pvpbot faction remove <faction> <player>`| Удалить из фракции |
| `/pvpbot faction hostile <f1> <f2> [true/false]`| Установить фракции как враждебные |
| `/pvpbot faction addnear <faction> <radius>`| Добавить всех ближайших ботов |
| `/pvpbot faction give <faction> <item>`| Раздать предмет всем участникам |
| `/pvpbot faction givekit <faction> <kit>`| Раздайте комплект всем участникам |
| `/pvpbot faction attack <faction> <target>`| Все боты фракции атакуют цель |
| `/pvpbot faction follow <faction> <target>`| Все боты во фракции следуют за целью |
| `/pvpbot faction escort <faction> <target>`| Все боты в цели сопровождения фракции |
| `/pvpbot faction goto <faction> <x> <y> <z>`| Переместить всех ботов фракции в координаты |
| `/pvpbot faction startpath <faction> <path>`| Стартовый путь для всех ботов во фракции |
| `/pvpbot faction stoppath <faction>`| Остановить путь для всех ботов во фракции |
| `/pvpbot faction list`| Список всех фракций |
| `/pvpbot faction info <faction>`| Показать детали фракции |

### Примеры

```mcfunction
# Create two factions
/pvpbot faction create RedTeam
/pvpbot faction create BlueTeam

# Add bots to factions
/pvpbot faction add RedTeam Bot1
/pvpbot faction add BlueTeam Bot2

# Make them enemies
/pvpbot faction hostile RedTeam BlueTeam

# Order entire faction to attack
/pvpbot faction attack RedTeam Steve

# Make entire faction follow a player
/pvpbot faction follow RedTeam Alex

# Make entire faction escort a player
/pvpbot faction escort RedTeam Steve

# Move entire faction to coordinates
/pvpbot faction goto RedTeam 100 64 200

# Give swords to everyone in RedTeam
/pvpbot faction give RedTeam diamond_sword

# Make entire faction patrol a path
/pvpbot faction startpath RedTeam patrol_route

# Stop faction from patrolling
/pvpbot faction stoppath RedTeam
```

---

## 🎒 Команды набора

| Команда | Описание |
|---------|-------------|
| `/pvpbot createkit <name>`| Создать комплект из своего инвентаря |
| `/pvpbot deletekit <name>`| Удалить комплект |
| `/pvpbot kits`| Список всех комплектов |
| `/pvpbot givekit <bot> <kit>`| Отдать комплект боту |
| `/pvpbot faction givekit <faction> <kit>`| Отдать комплект фракции |

### Примеры

```mcfunction
# Put items in your inventory, then:
/pvpbot createkit warrior

# Give kit to a bot
/pvpbot givekit Bot1 warrior

# Give kit to entire faction
/pvpbot faction givekit RedTeam warrior
```

---

## 🛤️ Команды пути

| Команда | Описание |
|---------|-------------|
| `/pvpbot path create <name>`| Создать новый путь |
| `/pvpbot path delete <name>`| Удалить путь |
| `/pvpbot path addpoint <name>`| Добавить текущую позицию в качестве путевой точки |
| `/pvpbot path removepoint <name> [index]`| Удалить путевую точку (последнюю или по индексу) |
| `/pvpbot path clear <name>`| Удалить все путевые точки |
| `/pvpbot path list`| Список всех путей |
| `/pvpbot path info <name>`| Показать информацию о пути |
| `/pvpbot path start <bot> <path>`| Заставить бота следовать по пути |
| `/pvpbot path stop <bot>`| Не дать боту следовать по пути |
| `/pvpbot path loop <name> <true/false>`| Переключить режим цикла |
| `/pvpbot path attack <name> <true/false>`| Переключить боевой режим |
| `/pvpbot path show <name> <true/false>`| Переключить визуализацию пути |
| `/pvpbot path distribute <path>`| Распределите ботов равномерно по пути |
| `/pvpbot path startnear <path> <radius>`| Стартовый путь для ботов в радиусе |
| `/pvpbot path stopall <path>`| Остановить всех ботов на этом пути |

### Примеры

```mcfunction
# Create a patrol route
/pvpbot path create patrol

# Add waypoints (stand at each location)
/pvpbot path addpoint patrol
/pvpbot path addpoint patrol
/pvpbot path addpoint patrol

# Make bot follow the path
/pvpbot path start Guard1 patrol

# Enable back-and-forth movement
/pvpbot path loop patrol true

# Disable combat while patrolling
/pvpbot path attack patrol false

# Show path with particles
/pvpbot path show patrol true

# Distribute all bots on path evenly
/pvpbot path distribute patrol

# Start path for all bots within 50 blocks
/pvpbot path startnear patrol 50

# Stop all bots following this path
/pvpbot path stopall patrol
```

Подробное руководство см. на странице [Пути](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Paths).

---

## ⚙️ Настройки

Использовать`/pvpbot settings`чтобы увидеть все текущие настройки.

Использовать`/pvpbot settings <setting>`чтобы увидеть текущее значение.

Использовать`/pvpbot settings <setting> <value>`чтобы изменить настройку.

Использовать`/pvpbot settings gui`чтобы открыть меню графических настроек.

Полный список всех настроек см. на странице [Настройки](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Settings).

### Быстрые примеры

```mcfunction
# Enable auto-targeting
/pvpbot settings autotarget true

# Set miss chance to 20%
/pvpbot settings misschance 20

# Enable bunny hop
/pvpbot settings bhop true
```
