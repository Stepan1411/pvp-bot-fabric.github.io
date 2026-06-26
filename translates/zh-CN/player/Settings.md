#⚙️设置

所有配置选项的完整列表。

---

## 📋 命令

```mcfunction
# Show all settings
/pvpbot settings

# Show specific setting
/pvpbot settings <name>

# Change setting
/pvpbot settings <name> <value>
```

---

## ⚔️ 战斗设置

|设置|类型 |范围 |默认|描述 |
|--------|------|--------|---------|------------|
| `combat`|布尔 | - |真实 |启用/禁用战斗系统 |
| `revenge`|布尔 | - |真实 |攻击损害机器人的实体 |
| `autotarget`|布尔 | - |假 |自动搜索敌人 |
| `targetplayers`|布尔 | - |真实 |可以针对玩家|
| `targetmobs`|布尔 | - |假 |可以瞄准敌对生物 |
| `targetbots`|布尔 | - |假 |可以针对其他机器人 |
| `criticals`|布尔 | - |真实 |执行致命一击 |
| `ranged`|布尔 | - |真实 |使用弓/弩 |
| `mace`|布尔 | - |真实 |使用带有风弹的狼牙棒 |
| `spear`|布尔 | - |假 |使用矛（由于地毯错误而禁用）|
| `crystalpvp`|布尔 | - |假 |使用水晶PVP（黑曜石+水晶）|
| `anchorpvp`|布尔 | - |假 |使用锚点 PVP（重生锚点 + 萤石）|
| `elytramace`|布尔 | - |真实 |使用鞘翅锤技巧（鞘翅 + 狼牙棒）|
| `attackcooldown`|整数 | 1-40 | 1-40 10 | 10攻击之间的滴答声|
| `meleerange`|双| 2-6 | 2-6 3.5 | 3.5近战攻击距离|
| `movespeed`|双| 0.1-2.0 | 1.0 |移动速度倍增|
| `viewdistance`|双| 5-128 | 5-128 64 | 64最大目标检测范围|
| `retreat`|布尔 | - |真实 | HP低时撤退|
| `retreathp`|双| 0.1-0.9| 0.3 | 0.3开始撤退的HP百分比（30%）|

---

## 🧪 药水设置

|设置|类型 |范围 |默认|描述 |
|--------|------|--------|---------|------------|
| `autopotion`|布尔 | - |真实 |自动使用治疗/增益药水|
| `cobweb`|布尔 | - |真实 |使用蜘蛛网来减缓敌人的速度 |

机器人自动使用：
- **生命值低时的治疗药水**
- **进入战斗时的力量药水**
- 进入战斗时**速度药水**
- **进入战斗时抗火药水**
- **蜘蛛网**减慢敌人的速度（当撤退或敌人冲锋时）

当战斗开始或效果到期时，所有增益药水都会立即抛出。

---

## 🚶 导航设置

|设置|类型 |范围 |默认|描述 |
|--------|------|--------|---------|------------|
| `bhop`|布尔 | - |真实 |启用兔子跳 |
| `bhopcooldown`|整数 | 5-30 | 12 | 12 bhop 跳跃之间的滴答声 |
| `jumpboost`|双| 0.0-0.5 | 0.0 | 0.0额外跳跃高度|
| `idle`|布尔 | - |真实 |没有目标就流浪|
| `idleradius`|双| 3-50 | 3-50 10 | 10怠速漂移半径|

---

## 🛡️设备设置

|设置|类型 |范围 |默认|描述 |
|--------|------|--------|---------|------------|
| `autoarmor`|布尔 | - |真实 |自动装备最好的装甲|
| `autoweapon`|布尔 | - |真实 |自动装备最好的武器|
| `autototem`|布尔 | - |真实 |副手自动装备图腾|
| `totempriority`|布尔 | - |真实 |图腾优先于盾牌|
| `autoshield`|布尔 | - |真实 |格挡时自动使用护盾 |
| `automend`|布尔 | - |真实 |使用 XP 瓶自动修复装甲 |
| `menddurability`|双| 0.1-1.0 | 0.5 | 0.5耐用性修复百分比阈值 (50%) |
| `prefersword`|布尔 | - |真实 |比起斧子更喜欢剑 |
| `shieldbreak`|布尔 | - |真实 |切换到斧头打破敌人的盾牌 |
| `droparmor`|布尔 | - |假 |掉落更差的护甲碎片 |
| `dropweapon`|布尔 | - |假 |掉落更糟糕的武器 |
| `dropdistance`|双| 1-10 | 1-10 3.0 |物品拾取距离|
| `interval`|整数 | 1-100 | 1-100 20 |设备检查间隔（蜱）|
| `minarmorlevel`|整数 | 0-100 | 0 |装备的最低装甲等级 |

### 护甲等级
|水平|装甲类型 |
|--------|------------|
| 0 |任何铠甲 |
| 20 |皮革+ |
| 40|黄金+ |
| 50|链条+ |
| 60|铁+ |
| 80|钻石+ |
| 100 | 100仅限下界合金 |

---

## 🎭 真实感设置

|设置|类型 |范围 |默认|描述 |
|--------|------|--------|---------|------------|
| `misschance`|整数 | 0-100 | 10 | 10错过攻击的几率 (%) |
| `mistakechance`|整数 | 0-100 | 5 |攻击错误方向的几率 (%) |
| `reactiondelay`|整数 | 0-20 | 0 |反应前的延迟（滴答声）|

---

## 👥 其他设置

|设置|类型 |范围 |默认|描述 |
|--------|------|--------|---------|------------|
| `factions`|布尔 | - |真实 |启用派系系统 |
| `friendlyfire`|布尔 | - |假 |允许对派系盟友造成伤害 |
| `specialnames`|布尔 | - |假 |使用数据库中的特殊名称 |
| `gotousebaritone`|布尔 | - |假 |使用 Baritone 执行 goto 命令 |

---

## 🚀 鞘翅锤设置

|设置|类型 |范围 |默认|描述 |
|--------|------|--------|---------|------------|
| `elytramace`|布尔 | - |真实 |启用 ElytraMace 技巧 |
| `elytramaceretries`|整数 | 1-10 | 1-10 1 |最大起飞重试次数 |
| `elytramacealtitude`|整数 | 5-50 | 20 |最低攻击高度 |
| `elytramacedistance`|双| 3-15 | 3-15 8.0 |距目标的攻击距离|
| `elytramacefireworks`|整数 | 1-10 | 1-10 3 |使用烟花数量|

**鞘翅狼牙棒技巧：** 机器人装备鞘翅，使用烟花飞起来，去除半空中的鞘翅，并用狼牙棒攻击造成大量坠落伤害。

---

## 💾 配置文件

设置保存在：
```
config/pvp_bot.json
```

机器人数据（位置、尺寸、游戏模式）保存在：
```
config/pvp_bot_bots.json
```

设置和机器人在服务器重新启动后仍然存在。服务器启动时，机器人会自动恢复。

---

## 📋 示例

### 让机器人更加真实
```mcfunction
/pvpbot settings misschance 15
/pvpbot settings mistakechance 10
/pvpbot settings reactiondelay 5
```

### 让机器人具有攻击性
```mcfunction
/pvpbot settings autotarget true
/pvpbot settings targetplayers true
/pvpbot settings targetbots true
/pvpbot settings revenge true
```

### 禁用远程战斗
```mcfunction
/pvpbot settings ranged false
/pvpbot settings mace false
/pvpbot settings crystalpvp false
/pvpbot settings anchorpvp false
```

### 快速移动
```mcfunction
/pvpbot settings bhop true
/pvpbot settings bhopcooldown 8
/pvpbot settings jumpboost 0.2
/pvpbot settings movespeed 1.5
```

### 固定警卫
```mcfunction
/pvpbot settings idle false
/pvpbot settings bhop false
```

### 启用 ElytraMace 技巧
```mcfunction
/pvpbot settings elytramace true
/pvpbot settings elytramacealtitude 25
/pvpbot settings elytramaceretries 2
```

### 使用 Baritone 启用移动命令
```mcfunction
/pvpbot settings gotousebaritone true
```

### 启用特殊名称
```mcfunction
/pvpbot settings specialnames true
```
