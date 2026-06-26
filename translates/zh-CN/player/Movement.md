# 🚶 Movement System

PVP 机器人具有先进的运动系统，允许机器人跟随玩家、护送目标并导航到特定坐标。

---

## 🎯 Movement Modes

### Follow Mode
Bots follow a target while maintaining optimal distance.

```mcfunction
# Make bot follow a player
/pvpbot follow Bot1 Steve

# Make bot follow another bot
/pvpbot follow Bot1 Bot2
```

**Behavior:**
- Maintains 3-block distance from target
- 自动避开障碍物
- 跨维度追随
- 使用智能寻路
- 当目标离线时停止

### 护送模式
增强跟随模式与防御能力。

```mcfunction
# Make bot escort a player
/pvpbot escort Bot1 Steve

# Make bot escort another bot
/pvpbot escort Bot1 Bot2
```

**行为：**
- 与跟随模式相同
- **如果受到攻击，自动防御目标**
- 优先考虑目标保护而不是其他战斗
- 攻击任何伤害护送目标的人

### 转到模式
直接基于坐标的运动。

```mcfunction
# Send bot to coordinates
/pvpbot goto Bot1 100 64 200

# Use relative coordinates
/pvpbot goto Bot1 ~10 ~ ~-5
```

**行为：**
- 智能寻路坐标
- 躲避障碍和跳跃
- 可选的男中音集成
- 到达目的地时停止

---

## 🛑 停止运动

```mcfunction
# Stop any movement mode
/pvpbot stopmovement Bot1
```

该命令停止：
- 跟随模式
- 护送模式
- 转到模式
- 路径跟踪

---

## 👥 派系运动

所有移动命令都适用于派系：

```mcfunction
# Make entire faction follow a target
/pvpbot faction follow RedTeam Steve

# Make entire faction escort a target
/pvpbot faction escort RedTeam Steve

# Move entire faction to coordinates
/pvpbot faction goto RedTeam 100 64 200
```

---

## ⚙️ 动作设置

|设置|类型 |范围 |默认|描述 |
|--------|------|--------|---------|------------|
| `movespeed`|双| 0.1-2.0 | 1.0 |基础移动速度|
| `bhop`|布尔 | - |真实 |启用兔子跳 |
| `bhopcooldown`|整数 | 5-30 | 12 | 12跳跃之间的刻度|
| `jumpboost`|双| 0.0-0.5 | 0.0 | 0.0额外跳跃高度|
| `gotousebaritone`|布尔 | - |假 |使用 Baritone 进行 goto |

---

## 🧭 男中音整合

启用 Baritone 进行高级寻路：

```mcfunction
/pvpbot settings gotousebaritone true
```

**好处：**
- 复杂地形导航
- 远距离寻路
- 自动桥梁建设
- 穿越障碍物采矿

**要求：**
- 必须安装男中音模组
- 仅适用于 goto 命令
- 可能比基本寻路慢

---

## 🔧 技术细节

### 跟随距离
- **目标距离：** 3 个街区
- **停止距离：** 2 个街区
- **最大距离：** 50 个方块（超出则传送）

### 更新频率
- 运动每次更新（每秒 20 次）
- 每 5 个刻度检查一次目标位置
- 需要时重新计算寻路

### 障碍物处理
- 自动跳过1格障碍物
- 在墙壁和障碍物周围寻路
- 在水中游泳
- 攀爬梯子和藤蔓

---

## 🚨 故障排除

### 机器人不关注
- 检查目标是否存在并且在线
- 验证机器人没有卡住或被阻止
- 确保运动未被禁用
- 检查机器人是否处于战斗状态（可能会覆盖移动）

### 机器人被卡住
- 使用`/pvpbot stopmovement`并重新启动
- 为复杂地形启用男中音
- 检查是否有障碍物阻挡路径
- 传送机器人到清理区域

### 护送不防守
- 验证护送模式是否处于活动状态（不仅仅是跟随）
- 检查友军火力是否被禁用
- 确保机器人拥有武器和战斗能力
- 目标必须实际受到伤害才能触发防御

---

## 💡 使用技巧

### 有效关注
- 在开放区域使用以获得最佳效果
- 避免拥挤或复杂的地形
- 保持目标以合理的速度移动
- 为重要玩家提供护送

### 坐标导航
- 使用goto进行精确定位
- 长距离启用男中音
- 检查坐标是否可访问
- 使用相对坐标进行附近的移动

### 派系协调
- 使用派系命令组织大型团体
- 使用护卫来保护 VIP
- 与派系 goto 协调攻击
- 通过交错命令分散到达时间