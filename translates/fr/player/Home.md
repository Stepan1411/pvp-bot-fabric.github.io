# 🤖 Bot PVP - Wiki

Bienvenue dans la documentation officielle du Bot PVP !

---

## 📖 About

PVP Bot est un mod Minecraft Fabric qui ajoute des robots de combat intelligents alimentés par le mod HeroBot. Créez des armées de robots, organisez-les en factions et regardez des batailles épiques se dérouler !

---

## 🚀 Quick Start

1. Installez [Fabric Loader](https://fabricmc.net/) et [HeroBot Mod](https://modrinth.com/mod/herobot)
2. Téléchargez PVP Bot et placez-le dans votre`mods`dossier
3. Démarrez le jeu et utilisez`/pvpbot spawn BotName`pour créer votre premier bot !

---

## 📚 Documentation

| Pages | Descriptif |
|------|-------------|
| [🎮 Commandes](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Commands) | Toutes les commandes disponibles |
| [⚔️ Système de combat](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Combat) | Comment les robots se battent |
| [💥 Combat explosif](https://github.com/Stepan1411/pvp-bot-fabric/wiki/ExplosiveCombat) | Cristal PVP et Ancre PVP |
| [🚀 ElytraMace](https://github.com/Stepan1411/pvp-bot-fabric/wiki/ElytraMace) | Technique avancée de combat aérien |
| [🚶Navigation](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Navigation) | Orientation de base |
| [🏃 Mouvement](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Movement) | Commandes suivre, escorter et aller à |
| [🛤️ Chemins](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Paths) | Système de chemins et waypoints |
| [👥 Factions](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Factions) | Système d'équipe |
| [🎒Kits](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Kits) | Préréglages d'équipement |
| [⚙️ Paramètres](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Settings) | Toutes les options de configuration |

---

## 💡 Exemples rapides

### Créer un bot simple
```
/pvpbot spawn MyBot
```

### Activer le PVP Cristal
```
/pvpbot settings crystalpvp true
```

### Activer l'astuce ElytraMace
```
/pvpbot settings elytramace true
```

### Faire en sorte que le bot suive un joueur
```
/pvpbot follow Bot1 Steve
```

### Faire en sorte qu'un bot escorte (suivre + protéger) un joueur
```
/pvpbot escort Bot1 Steve
```

### Faites combattre deux équipes
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

## 🔗 Liens

- [GitHub Repository](https://github.com/Stepan1411/pvp-bot-fabric)
- [Modrinth Page](https://modrinth.com/mod/pvp-bot)
- [Rapports de bugs](https://github.com/Stepan1411/pvp-bot-fabric/issues)
