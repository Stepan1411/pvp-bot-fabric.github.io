#⚔️战斗系统

PVP Bot 具有先进的战斗人工智能，可以使用不同的武器和战术。

---

## 🗡️ 武器类型

### Melee Combat
- **剑** - 快速攻击，良好的伤害
- **斧头** - 速度较慢，但​​可以打破护盾
- Bots automatically switch to melee when enemies are close

### 远程战斗
- **弓** - 绘制并释放箭头
- **十字弓** - 加载和消防螺栓
- 机器人保持最佳距离（8-20 个街区）

### 狼牙棒战斗
- **Mace + Wind Charge** - Jump attacks for massive damage
- 机器人利用风能发射到空中
- 毁灭性的坠落攻击

### 鞘翅狼牙棒战斗
- **鞘翅 + 狼牙棒 + 烟花** - 高级空中攻击技术
- 机器人装备鞘翅，使用烟花获得高度
- 在空中移除鞘翅并用狼牙棒攻击造成大量坠落伤害
- 可用时选择最高优先级的武器
- 可配置的高度、距离和重试设置

### 水晶 PVP
- **末地水晶 + 黑曜石** - 放置黑曜石并引爆水晶
- 机器人计算安全爆炸距离
- 自动水晶放置和引爆
- 高伤害爆炸战斗

### 主播 PVP
- **重生锚 + 萤石** - 主世界/末地的爆炸武器
- 机器人用萤石给锚充电
- 引爆造成巨大伤害
- 只能在下界之外使用

---

## 🎯 定位

### 复仇模式
当机器人受到伤害时，它会自动瞄准攻击者。
```mcfunction
/pvpbot settings revenge true
```

### Auto-Target
Bots automatically search for enemies within view distance.
```mcfunction
/pvpbot settings autotarget true
```

### 手动目标
Force a bot to attack a specific target.
```mcfunction
/pvpbot attack BotName TargetName
```

### Target Filters
Choose what bots can target:
```mcfunction
/pvpbot settings targetplayers true   # Target players
/pvpbot settings targetmobs true      # Target hostile mobs
/pvpbot settings targetbots true      # Target other bots
```

---

## 🛡️ Defense

### 自动屏蔽
当敌人攻击时，机器人会自动举起护盾。
```mcfunction
/pvpbot settings autoshield true
```

### 破盾
机器人使用斧头来禁用敌人的护盾。
```mcfunction
/pvpbot settings shieldbreak true
```

### 自动图腾
机器人会随时保存不死图腾。
```mcfunction
/pvpbot settings autototem true
/pvpbot settings totempriority true  # Prioritize totem over shield
```

### 自动修复
机器人使用 XP 瓶自动修复受损的装甲。
```mcfunction
/pvpbot settings automend true
/pvpbot settings menddurability 0.5  # Repair at 50% durability
```

---

## 🍎 治愈

### 自动吃
机器人在以下情况下吃食物：
- 健康状况不佳 (< 30%)
- 饥饿低于阈值

```mcfunction
/pvpbot settings autoeat true
/pvpbot settings minhunger 14
```

### 自动药水
机器人自动使用药水：
- **治疗药水** - 当HP较低时（飞溅或饮用）
- **力量药水** - 进入战斗时
- **速度药水** - 进入战斗时
- **抗火药水** - 进入战斗时

战斗开始时，所有增益药水都会立即投入。当效果到期时（剩余 < 5 秒），机器人会重新应用增益。

```mcfunction
/pvpbot settings autopotion true
```

### 撤退
当生命值较低时，机器人会在进食/治疗时撤退。
如果机器人没有食物（战斗至死），则无法撤退。

```mcfunction
/pvpbot settings retreat true
/pvpbot settings retreathp 0.3  # 30% HP
```

---

## 💥 热门歌曲

机器人可以通过跳跃攻击来进行致命一击。
```mcfunction
/pvpbot settings criticals true
```

---

## 🕸️ 蛛网战术

机器人可以战略性地使用蜘蛛网：
- **撤退时** - 将蜘蛛网放置在追逐敌人的下方以减慢他们的速度
- **在近战战斗中** - 将蜘蛛网放置在冲锋的敌人下方

```mcfunction
/pvpbot settings cobweb true
```

---

## ⚙️ 战斗设置

|设置|范围 |默认|描述 |
|--------|--------|---------|------------|
| `combat`|真/假|真实 |启用战斗 |
| `revenge`|真/假|真实 |攻击攻击你的人 |
| `autotarget`|真/假|假 |自动寻找敌人 |
| `criticals`|真/假|真实 |严重打击 |
| `ranged`|真/假|真实 |使用弓|
| `mace`|真/假|真实 |使用狼牙棒|
| `spear`|真/假|假 |使用长矛（越野车）|
| `crystalpvp`|真/假|假 |使用水晶PVP |
| `anchorpvp`|真/假|假 |使用主播PVP |
| `elytramace`|真/假|真实 |使用鞘翅锤技巧 |
| `autopotion`|真/假|真实 |自动使用药水 |
| `automend`|真/假|真实 |自动修复装甲|
| `menddurability`| 0.1-1.0 | 0.5 | 0.5修复耐久性% |
| `totempriority`|真/假|真实 |盾牌上的图腾|
| `cobweb`|真/假|真实 |使用蜘蛛网 |
| `retreat`|真/假|真实 | HP低时撤退|
| `retreathp`| 0.1-0.9| 0.3 | 0.3 HP % 撤退 |
| `attackcooldown`| 1-40 | 1-40 10 | 10攻击之间的滴答声|
| `meleerange`| 2-6 | 2-6 3.5 | 3.5近战攻击距离|
| `viewdistance`| 5-128 | 5-128 64 | 64目标搜索范围|
