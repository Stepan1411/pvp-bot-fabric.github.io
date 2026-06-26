# 🎮 Commandes

Toutes les commandes du Bot PVP commencent par`/pvpbot`. Nécessite le niveau d'autorisation 2 (opérateur).

---

## 📋 Table of Contents

- [Gestion des robots](#-bot-management)
- [Commandes de combat](#-combat-commands)
- [Faction Commands](#-faction-commands)
- [Commandes du kit](#-kit-commandes)
- [Commandes de chemin](#-path-commands)
- [Paramètres](#-paramètres)

---

## 🤖 Gestion des robots

| Command | Description |
|---------|-------------|
| `/pvpbot spawn [name]`| Créer un nouveau bot (nom aléatoire si non spécifié) |
| `/pvpbot massspawn <count>`| Générez plusieurs robots avec des noms aléatoires (1-50) |
| `/pvpbot remove <name>`| Supprimer un robot |
| `/pvpbot removeall`| Supprimer tous les robots |
| `/pvpbot list`| Lister tous les robots actifs |
| `/pvpbot menu`| Ouvrir le menu de l'interface graphique |
| `/pvpbot inventory <name>`| Afficher l'inventaire du bot |

### Exemples

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

**Remarque :** Lorsque vous générez des robots avec des noms aléatoires, il y a 10 % de chances qu'ils obtiennent un nom spécial (`nantag`ou`Stepan1411`) au lieu d'un nom généré.

---

## ⚔️ Commandes de combat

| Commande | Descriptif |
|---------|-------------|
| `/pvpbot attack <bot> <target>`| Ordonner au bot d'attaquer un joueur/une entité |
| `/pvpbot stop <bot>` | Stop bot from attacking |
| `/pvpbot target <bot>`| Afficher la cible actuelle du bot |

---

## 🚶 Movement Commands

| Command | Description |
|---------|-------------|
| `/pvpbot follow <bot> <target>` | Make bot follow a player/bot |
| `/pvpbot escort <bot> <target>`| Faire en sorte que le bot suive et protège une cible |
| `/pvpbot goto <bot> <x> <y> <z>`| Déplacer le bot vers des coordonnées spécifiques |
| `/pvpbot stopmovement <bot>`| Arrêter le mouvement du robot |

### Exemples de mouvements

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

**Note:**
- **Suivre** : le robot maintient une distance de 3 blocs par rapport à la cible
- **Escorte** : Idem que ci-dessous, mais le bot défendra la cible s'il est attaqué.
- **Goto** : le robot se déplace vers les coordonnées à l'aide de la recherche de chemin intelligente (baryton si activé)

### Exemples

```mcfunction
# Make Bot1 attack player Steve
/pvpbot attack Bot1 Steve

# Stop the attack
/pvpbot stop Bot1

# Check who Bot1 is targeting
/pvpbot target Bot1
```

---

## 👥 Commandes de faction

| Commande | Descriptif |
|---------|-------------|
| `/pvpbot faction create <name>`| Créer une nouvelle faction |
| `/pvpbot faction delete <name>`| Supprimer une faction |
| `/pvpbot faction add <faction> <player>`| Ajouter un joueur/bot à la faction |
| `/pvpbot faction remove <faction> <player>`| Retirer de la faction |
| `/pvpbot faction hostile <f1> <f2> [true/false]`| Définir les factions comme hostiles |
| `/pvpbot faction addnear <faction> <radius>`| Ajouter tous les robots à proximité |
| `/pvpbot faction give <faction> <item>`| Donner l'article à tous les membres |
| `/pvpbot faction givekit <faction> <kit>`| Offrez un kit à tous les membres |
| `/pvpbot faction attack <faction> <target>`| Tous les robots de la faction attaquent la cible |
| `/pvpbot faction follow <faction> <target>`| Tous les robots de la faction suivent la cible |
| `/pvpbot faction escort <faction> <target>`| Tous les robots de la faction escortent la cible |
| `/pvpbot faction goto <faction> <x> <y> <z>`| Déplacez tous les robots de la faction vers les coordonnées |
| `/pvpbot faction startpath <faction> <path>`| Chemin de départ pour tous les robots de la faction |
| `/pvpbot faction stoppath <faction>`| Chemin d'arrêt pour tous les robots de la faction |
| `/pvpbot faction list`| Liste toutes les factions |
| `/pvpbot faction info <faction>`| Afficher les détails de la faction |

### Exemples

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

## 🎒 Commandes du kit

| Commande | Descriptif |
|---------|-------------|
| `/pvpbot createkit <name>`| Créez un kit à partir de votre inventaire |
| `/pvpbot deletekit <name>`| Supprimer un kit |
| `/pvpbot kits`| Liste de tous les kits |
| `/pvpbot givekit <bot> <kit>`| Donner un kit à un bot |
| `/pvpbot faction givekit <faction> <kit>`| Donner le kit à la faction |

### Exemples

```mcfunction
# Put items in your inventory, then:
/pvpbot createkit warrior

# Give kit to a bot
/pvpbot givekit Bot1 warrior

# Give kit to entire faction
/pvpbot faction givekit RedTeam warrior
```

---

## 🛤️ Commandes de chemin

| Commande | Descriptif |
|---------|-------------|
| `/pvpbot path create <name>`| Créer un nouveau chemin |
| `/pvpbot path delete <name>`| Supprimer un chemin |
| `/pvpbot path addpoint <name>`| Add current position as waypoint |
| `/pvpbot path removepoint <name> [index]`| Supprimer un waypoint (dernier ou par index) |
| `/pvpbot path clear <name>`| Supprimer tous les waypoints |
| `/pvpbot path list`| Liste tous les chemins |
| `/pvpbot path info <name>`| Afficher les informations sur le chemin |
| `/pvpbot path start <bot> <path>`| Faire en sorte que le bot suive le chemin |
| `/pvpbot path stop <bot>`| Empêcher le bot de suivre le chemin |
| `/pvpbot path loop <name> <true/false>`| Basculer le mode boucle |
| `/pvpbot path attack <name> <true/false>`| Basculer le mode combat |
| `/pvpbot path show <name> <true/false>`| Basculer la visualisation du chemin |
| `/pvpbot path distribute <path>`| Répartir les robots uniformément le long du chemin |
| `/pvpbot path startnear <path> <radius>`| Chemin de départ pour les robots dans le rayon |
| `/pvpbot path stopall <path>`| Arrêtez tous les robots sur ce chemin |

### Exemples

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

Voir la page [Chemins](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Paths) pour un guide détaillé.

---

## ⚙️ Paramètres

Utiliser`/pvpbot settings`pour voir tous les paramètres actuels.

Utiliser`/pvpbot settings <setting>`pour voir la valeur actuelle.

Utiliser`/pvpbot settings <setting> <value>`pour modifier un paramètre.

Utiliser`/pvpbot settings gui`pour ouvrir le menu des paramètres graphiques.

Voir la page [Paramètres](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Settings) pour la liste complète de tous les paramètres.

### Exemples rapides

```mcfunction
# Enable auto-targeting
/pvpbot settings autotarget true

# Set miss chance to 20%
/pvpbot settings misschance 20

# Enable bunny hop
/pvpbot settings bhop true
```
