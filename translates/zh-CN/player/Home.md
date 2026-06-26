# 🤖 PVP 机器人 - 维基

欢迎来到官方 PVP 机器人文档！

---

## 📖 About

PVP Bot 是一个 Minecraft Fabric 模组，添加了由 HeroBot 模组提供支持的智能战斗机器人。创建机器人大军，将他们组织成派系，观看史诗般的战斗展开！

---

## 🚀 Quick Start

1.安装[Fabric Loader](https://fabricmc.net/)和[HeroBot Mod](https://modrinth.com/mod/herobot)
2.下载PVP Bot并将其放入您的`mods`文件夹
3.启动游戏并使用`/pvpbot spawn BotName`创建您的第一个机器人！

---

## 📚 Documentation

|页 |描述 |
|------|-------------|
| [🎮 命令](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Commands) |所有可用命令 |
| [⚔️战斗系统](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Combat) |机器人如何战斗 |
| [💥 爆炸战斗](https://github.com/Stepan1411/pvp-bot-fabric/wiki/ExplosiveCombat) |水晶 PVP 和锚 PVP |
| [🚀 ElytraMace](https://github.com/Stepan1411/pvp-bot-fabric/wiki/ElytraMace) |先进空战技术|
| [🚶 导航](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Navigation) |基本寻路 |
| [🏃 运动](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Movement) |跟随、护送和转到命令 |
| [🛤️ 路径](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Paths) |路径系统和航路点|
| [👥 派系](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Factions) |团队体系|
| [🎒 套件](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Kits) |设备预设|
| [⚙️ 设置](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Settings) |所有配置选项|

---

## 💡 简单示例

### 创建一个简单的机器人
```
/pvpbot spawn MyBot
```

### 启用水晶 PVP
```
/pvpbot settings crystalpvp true
```

### 启用 ElytraMace 技巧
```
/pvpbot settings elytramace true
```

### 让机器人跟随玩家
```
/pvpbot follow Bot1 Steve
```

### 让机器人护送（跟随+保护）玩家
```
/pvpbot escort Bot1 Steve
```

### 让两队战斗
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

## 🔗 链接

- [GitHub 存储库](https://github.com/Stepan1411/pvp-bot-fabric)
- [Modrinth Page](https://modrinth.com/mod/pvp-bot)
- [Bug Reports](https://github.com/Stepan1411/pvp-bot-fabric/issues)
