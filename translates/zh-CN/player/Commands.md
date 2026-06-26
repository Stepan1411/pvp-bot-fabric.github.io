# 🎮 命令

所有 PVP Bot 命令均以以下开头`/pvpbot`。需要 2 级权限（操作员）。

---

## 📋 Table of Contents

- [Bot Management](#-bot-management)
- [战斗命令](#-combat-commands)
- [Faction Commands](#-faction-commands)
- [套件命令](#-kit-commands)
- [路径命令](#-path-commands)
- [设置](#-设置)

---

## 🤖 机器人管理

| Command | Description |
|---------|-------------|
| `/pvpbot spawn [name]`|创建一个新机器人（如果未指定，则为随机名称）|
| `/pvpbot massspawn <count>`|生成多个具有随机名称的机器人 (1-50) |
| `/pvpbot remove <name>`|删除机器人 |
| `/pvpbot removeall`|删除所有机器人 |
| `/pvpbot list`|列出所有活跃的机器人 |
| `/pvpbot menu`|打开 GUI 菜单 |
| `/pvpbot inventory <name>`|显示机器人的库存 |

### 示例

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

**注意：** 当生成具有随机名称的机器人时，它们有 10% 的机会获得特殊名称（`nantag`或者`Stepan1411`) 而不是生成的名称。

---

## ⚔️ 战斗命令

|命令 |描述 |
|---------|-------------|
| `/pvpbot attack <bot> <target>` | Order bot to attack a player/entity |
| `/pvpbot stop <bot>` | Stop bot from attacking |
| `/pvpbot target <bot>` | Show bot's current target |

---

## 🚶 Movement Commands

| Command | Description |
|---------|-------------|
| `/pvpbot follow <bot> <target>`|让机器人跟随玩家/机器人 |
| `/pvpbot escort <bot> <target>`|让机器人跟踪并保护目标 |
| `/pvpbot goto <bot> <x> <y> <z>`|将机器人移动到特定坐标 |
| `/pvpbot stopmovement <bot>`|停止机器人移动 |

### 动作示例

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

**笔记：**
- **跟随**：机器人与目标保持 3 格距离
- **护送**：与以下相同，但如果受到攻击，机器人将保护目标
- **Goto**：机器人使用智能寻路移动到坐标（男中音，如果启用）

### 示例

```mcfunction
# Make Bot1 attack player Steve
/pvpbot attack Bot1 Steve

# Stop the attack
/pvpbot stop Bot1

# Check who Bot1 is targeting
/pvpbot target Bot1
```

---

## 👥 派系命令

|命令 |描述 |
|---------|-------------|
| `/pvpbot faction create <name>`|创建新派系|
| `/pvpbot faction delete <name>`|删除派别 |
| `/pvpbot faction add <faction> <player>`|将玩家/机器人添加到派系 |
| `/pvpbot faction remove <faction> <player>`|从派系中删除 |
| `/pvpbot faction hostile <f1> <f2> [true/false]`|将派系设置为敌对 |
| `/pvpbot faction addnear <faction> <radius>`|添加所有附近的机器人 |
| `/pvpbot faction give <faction> <item>`|向所有会员赠送物品|
| `/pvpbot faction givekit <faction> <kit>`|向所有会员赠送套件 |
| `/pvpbot faction attack <faction> <target>`|派系中的所有机器人都攻击目标 |
| `/pvpbot faction follow <faction> <target>`|派系中的所有机器人都遵循目标 |
| `/pvpbot faction escort <faction> <target>`|派系中的所有机器人护送目标 |
| `/pvpbot faction goto <faction> <x> <y> <z>`|将派系中的所有机器人移至坐标 |
| `/pvpbot faction startpath <faction> <path>`|派系中所有机器人的起始路径 |
| `/pvpbot faction stoppath <faction>`|阻止派系中所有机器人的路径 |
| `/pvpbot faction list`|列出所有派别 |
| `/pvpbot faction info <faction>`|显示派系详细信息 |

### 示例

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

## 🎒 套件命令

|命令 |描述 |
|---------|-------------|
| `/pvpbot createkit <name>`|从您的库存中创建套件 |
| `/pvpbot deletekit <name>`|删除套件 |
| `/pvpbot kits`|列出所有套件 |
| `/pvpbot givekit <bot> <kit>`|向机器人提供套件 |
| `/pvpbot faction givekit <faction> <kit>`|向派系提供套件 |

### 示例

```mcfunction
# Put items in your inventory, then:
/pvpbot createkit warrior

# Give kit to a bot
/pvpbot givekit Bot1 warrior

# Give kit to entire faction
/pvpbot faction givekit RedTeam warrior
```

---

## 🛤️ 路径命令

|命令 |描述 |
|---------|-------------|
| `/pvpbot path create <name>`|创建新路径 |
| `/pvpbot path delete <name>`|删除路径 |
| `/pvpbot path addpoint <name>`|添加当前位置作为航点 |
| `/pvpbot path removepoint <name> [index]`|删除航路点（最后一个或按索引）|
| `/pvpbot path clear <name>`|删除所有航点 |
| `/pvpbot path list`|列出所有路径 |
| `/pvpbot path info <name>`|显示路径信息 |
| `/pvpbot path start <bot> <path>`|让机器人遵循路径 |
| `/pvpbot path stop <bot>`|阻止机器人遵循以下路径 |
| `/pvpbot path loop <name> <true/false>`|切换循环模式 |
| `/pvpbot path attack <name> <true/false>`|切换战斗模式 |
| `/pvpbot path show <name> <true/false>`|切换路径可视化|
| `/pvpbot path distribute <path>`|沿路径均匀分布机器人 |
| `/pvpbot path startnear <path> <radius>`|半径内机器人的起始路径 |
| `/pvpbot path stopall <path>`|停止此路径上的所有机器人 |

### 示例

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

有关详细指南，请参阅[路径](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Paths)页面。

---

## ⚙️ 设置

使用`/pvpbot settings`查看所有当前设置。

使用`/pvpbot settings <setting>`查看当前值。

使用`/pvpbot settings <setting> <value>`更改设置。

使用`/pvpbot settings gui`打开图形设置菜单。

有关所有设置的完整列表，请参阅[设置](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Settings)页面。

### 简单示例

```mcfunction
# Enable auto-targeting
/pvpbot settings autotarget true

# Set miss chance to 20%
/pvpbot settings misschance 20

# Enable bunny hop
/pvpbot settings bhop true
```
