#💥爆炸战斗

PVP 机器人使用末地水晶和重生锚支持先进的爆炸性战斗策略。

---

## 💎 水晶 PVP

Crystal PVP is a high-damage combat technique using End Crystals and Obsidian.

### 它是如何运作的
1. 机器人将黑曜石放置在目标附近
2. Bot places End Crystal on the obsidian
3.机器人引爆水晶造成巨大爆炸伤害
4. 机器人计算安全距离以避免自我伤害

### 启用水晶 PVP
```mcfunction
/pvpbot settings crystalpvp true
```

＃＃＃ 要求
机器人的库存中需要：
- **Obsidian** - for crystal placement base
- **末地水晶** - 用于爆炸

### 战术
- 机器人与爆炸保持安全距离
- 自动水晶放置和引爆
- 适用于所有尺寸
- 高伤害输出（最多 20 颗心）

---

## 锚PVP

锚 PVP 在主世界和末日中使用重生锚作为爆炸性武器。

### 它是如何运作的
1. 机器人将重生锚放置在目标附近
2. 机器人用萤石给锚充电
3. 机器人尝试设置重生（触发爆炸）
4.对附近实体造成巨大伤害

### 启用锚点 PVP
```mcfunction
/pvpbot settings anchorpvp true
```

＃＃＃ 要求
机器人的库存中需要：
- **重生锚** - 爆炸装置
- **萤石** - 为锚充电

### 重要提示
- 仅适用于主世界和末地（不适用于下界）
- 在下界，锚正常工作（没有爆炸）
- Very high damage output
- Consumes anchor and glowstone per use

---

## ⚙️ 设置

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `crystalpvp` | bool | false | Enable Crystal PVP |
| `anchorpvp` | bool | false | Enable Anchor PVP |

---

## 💡 使用技巧

### 水晶 PVP
- 给机器人成堆的黑曜石和水晶
- 在中等范围（5-10 块）效果最佳
- 对装甲对手非常有效
- 可以突破护盾

### 主播 PVP
- 比水晶 PVP 更贵（每次使用都会消耗锚）
- 极高的伤害
- 最好用作终结技
- 储备萤石

### 组合策略
```mcfunction
# Enable all explosive combat
/pvpbot settings crystalpvp true
/pvpbot settings anchorpvp true

# Give bot supplies
/give @e[type=player,name=Bot1] obsidian 64
/give @e[type=player,name=Bot1] end_crystal 64
/give @e[type=player,name=Bot1] respawn_anchor 16
/give @e[type=player,name=Bot1] glowstone 64
```

---

## 🛡️ 安全

机器人自动：
- 计算安全爆炸距离
- 尽可能避免自我伤害
- 优先考虑目标伤害而不是自我保护
- 如果有的话，使用不朽图腾

---

## 🔗 相关页面

- [战斗系统](Combat.md) - 一般战斗机制
- [设置](Settings.md) - 所有配置选项
- [命令](Commands.md) - 命令参考
