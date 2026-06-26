# 🚶 Navigation System

PVP Bot features smart pathfinding, movement mechanics, and advanced movement commands.

---

## 🎯 Movement Commands

### Follow System
机器人可以跟随玩家或其他机器人，同时保持最佳距离：

```mcfunction
# Make bot follow a target
/pvpbot follow Bot1 Steve

# Stop following
/pvpbot stopmovement Bot1
```

**行为：**
- 与目标保持 3 格距离
- 自动避开障碍物
- 跨维度追踪目标
- 使用智能寻路

### 护送系统
增强跟随模式与防御能力：

```mcfunction
# Make bot escort (follow + protect) a target
/pvpbot escort Bot1 Steve
```

**行为：**
- 与跟随模式相同
- 受到攻击时自动防御目标
- 优先考虑目标保护而不是其他战斗

### 转到系统
直接基于坐标的运动：

```mcfunction
# Send bot to specific coordinates
/pvpbot goto Bot1 100 64 200

# Enable Baritone for advanced pathfinding
/pvpbot settings gotousebaritone true
```

**行为：**
- 智能寻路坐标
- 躲避障碍和跳跃
- 针对复杂路径的可选男中音集成
- 适用于不同的地形类型

---

## 🧭 寻路

### 避障
机器人自动检测并避免：
- **墙壁** - 左转/右转以绕行
- **洞** - 跳过间隙
- **1 格障碍** - 跳起来

### 攀岩
机器人可以攀爬：
- 梯子
- 藤蔓
- 脚手架
- 扭曲/哭泣的藤蔓

---

## 🐰 兔子跳 (Bhop)

机器人可以通过兔子跳来实现更快的移动——在冲刺时跳跃以提高速度。

```mcfunction
# Enable/disable bhop
/pvpbot settings bhop true

# Set cooldown between jumps (5-30 ticks)
/pvpbot settings bhopcooldown 12

# Add extra jump height (0.0-0.5)
/pvpbot settings jumpboost 0.1
```

### 当 Bhop 激活时
- 速度 >= 1.0
- 前方没有障碍
- 不攀爬
- 在地面上

---

## 😴 闲逛

当机器人没有目标时，它们会在生成点周围徘徊。

```mcfunction
# Enable/disable idle wandering
/pvpbot settings idle true

# Set wander radius (3-50 blocks)
/pvpbot settings idleradius 10
```

＃＃＃ 行为
- 机器人缓慢行走（不是冲刺）
- 保持在重生点的半径范围内
- 选择随机目的地
- 徘徊时避开障碍物

---

## 🏃 移动速度

不同的情况使用不同的速度：

|情况|速度|波普 |
|------------|------|------|
|闲逛| 0.5 | 0.5 ❌ |
|接近目标 | 1.0 | ✅ |
|吃饭（撤退）| 1.2 | 1.2 ✅ |
|低HP撤退| 1.5 | 1.5 ✅ |

---

## ⚙️ 导航设置

|设置|范围 |默认|描述 |
|--------|--------|---------|------------|
| `bhop`|真/假|真实 |启用兔子跳 |
| `bhopcooldown`| 5-30 | 12 | 12跳跃之间的刻度|
| `jumpboost`| 0.0-0.5 | 0.0 | 0.0额外跳跃高度|
| `idle`|真/假|真实 |启用空闲徘徊|
| `idleradius`| 3-50 | 3-50 10 | 10游走半径|
| `movespeed`| 0.1-2.0 | 1.0 |基础移动速度|
| `gotousebaritone`|真/假|假 |使用 Baritone 进行 goto |

---

## 🔧 故障排除

### 机器人被卡住
- 机器人会自动尝试摆脱束缚
- 10 次没有运动后它们会跳跃并改变方向
- 如果仍然卡住，请尝试传送机器人

### 机器人不会爬
- 确保梯子/藤蔓放置正确
- 机器人需要面向可攀爬的方块

### 机器人掉进洞里
- 机器人尝试跳过 2 个区块的间隙
- 较大的间隙可能会导致跌倒
- 考虑为重要路径搭建桥梁
