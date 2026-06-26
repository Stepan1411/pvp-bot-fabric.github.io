# 🎮 Befehle

Alle PVP-Bot-Befehle beginnen mit`/pvpbot`. Erfordert Berechtigungsstufe 2 (Bediener).

---

## 📋 Table of Contents

- [Bot Management](#-bot-management)
- [Kampfbefehle](#-combat-commands)
- [Faction Commands](#-faction-commands)
- [Kit-Befehle](#-kit-commands)
- [Pfadbefehle](#-pfadbefehle)
- [Einstellungen](#-Einstellungen)

---

## 🤖 Bot-Management

| Befehl | Beschreibung |
|---------|-------------|
| `/pvpbot spawn [name]`| Erstellen Sie einen neuen Bot (zufälliger Name, falls nicht angegeben) |
| `/pvpbot massspawn <count>`| Erzeuge mehrere Bots mit zufälligen Namen (1-50) |
| `/pvpbot remove <name>`| Einen Bot entfernen |
| `/pvpbot removeall`| Alle Bots entfernen |
| `/pvpbot list`| Alle aktiven Bots auflisten |
| `/pvpbot menu`| Öffnen Sie das GUI-Menü |
| `/pvpbot inventory <name>`| Bot-Inventar anzeigen |

### Beispiele

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

**Hinweis:** Beim Spawnen von Bots mit zufälligen Namen besteht eine 10-prozentige Chance, dass sie einen speziellen Namen erhalten (`nantag`oder`Stepan1411`) anstelle eines generierten Namens.

---

## ⚔️ Kampfbefehle

| Befehl | Beschreibung |
|---------|-------------|
| `/pvpbot attack <bot> <target>`| Bot befehlen, einen Spieler/eine Entität anzugreifen |
| `/pvpbot stop <bot>` | Stop bot from attacking |
| `/pvpbot target <bot>`| Aktuelles Ziel des Bots anzeigen |

---

## 🚶 Movement Commands

| Command | Description |
|---------|-------------|
| `/pvpbot follow <bot> <target>`| Bot einem Spieler/Bot folgen lassen |
| `/pvpbot escort <bot> <target>`| Lassen Sie den Bot einem Ziel folgen und es schützen |
| `/pvpbot goto <bot> <x> <y> <z>`| Bot zu bestimmten Koordinaten bewegen |
| `/pvpbot stopmovement <bot>`| Bot-Bewegung stoppen |

### Bewegungsbeispiele

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

**Notiz:**
- **Folgen**: Bot hält 3 Blocks Abstand zum Ziel
- **Eskorte**: Wie folgt, aber der Bot verteidigt das Ziel, wenn er angegriffen wird
- **Gehe zu**: Bot bewegt sich mithilfe intelligenter Pfadfindung zu Koordinaten (Bariton, falls aktiviert)

### Beispiele

```mcfunction
# Make Bot1 attack player Steve
/pvpbot attack Bot1 Steve

# Stop the attack
/pvpbot stop Bot1

# Check who Bot1 is targeting
/pvpbot target Bot1
```

---

## 👥 Fraktionsbefehle

| Befehl | Beschreibung |
|---------|-------------|
| `/pvpbot faction create <name>`| Erstelle eine neue Fraktion |
| `/pvpbot faction delete <name>`| Eine Fraktion löschen |
| `/pvpbot faction add <faction> <player>`| Spieler/Bot zur Fraktion hinzufügen |
| `/pvpbot faction remove <faction> <player>`| Aus Fraktion entfernen |
| `/pvpbot faction hostile <f1> <f2> [true/false]`| Fraktionen als feindlich festlegen |
| `/pvpbot faction addnear <faction> <radius>`| Alle Bots in der Nähe hinzufügen |
| `/pvpbot faction give <faction> <item>`| Artikel an alle Mitglieder weitergeben |
| `/pvpbot faction givekit <faction> <kit>`| Kit an alle Mitglieder weitergeben |
| `/pvpbot faction attack <faction> <target>`| Alle Bots in der Fraktion greifen Ziel an |
| `/pvpbot faction follow <faction> <target>`| Alle Bots in der Fraktion folgen dem Ziel |
| `/pvpbot faction escort <faction> <target>`| Alle Bots im Fraktionseskortziel |
| `/pvpbot faction goto <faction> <x> <y> <z>`| Verschiebe alle Bots der Fraktion zu den Koordinaten |
| `/pvpbot faction startpath <faction> <path>`| Startpfad für alle Bots in der Fraktion |
| `/pvpbot faction stoppath <faction>`| Stopppfad für alle Bots in der Fraktion |
| `/pvpbot faction list`| Alle Fraktionen auflisten |
| `/pvpbot faction info <faction>`| Fraktionsdetails anzeigen |

### Beispiele

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

## 🎒 Kit-Befehle

| Befehl | Beschreibung |
|---------|-------------|
| `/pvpbot createkit <name>`| Erstellen Sie ein Kit aus Ihrem Inventar |
| `/pvpbot deletekit <name>`| Ein Kit löschen |
| `/pvpbot kits`| Alle Kits auflisten |
| `/pvpbot givekit <bot> <kit>`| Kit einem Bot geben |
| `/pvpbot faction givekit <faction> <kit>`| Kit an Fraktion weitergeben |

### Beispiele

```mcfunction
# Put items in your inventory, then:
/pvpbot createkit warrior

# Give kit to a bot
/pvpbot givekit Bot1 warrior

# Give kit to entire faction
/pvpbot faction givekit RedTeam warrior
```

---

## 🛤️ Pfadbefehle

| Befehl | Beschreibung |
|---------|-------------|
| `/pvpbot path create <name>`| Erstellen Sie einen neuen Pfad |
| `/pvpbot path delete <name>`| Einen Pfad löschen |
| `/pvpbot path addpoint <name>`| Aktuelle Position als Wegpunkt hinzufügen |
| `/pvpbot path removepoint <name> [index]`| Wegpunkt entfernen (letzter oder nach Index) |
| `/pvpbot path clear <name>`| Alle Wegpunkte entfernen |
| `/pvpbot path list`| Alle Pfade auflisten |
| `/pvpbot path info <name>`| Pfadinformationen anzeigen |
| `/pvpbot path start <bot> <path>`| Bot dem Pfad folgen lassen |
| `/pvpbot path stop <bot>`| Bot daran hindern, dem Pfad zu folgen |
| `/pvpbot path loop <name> <true/false>`| Loop-Modus umschalten |
| `/pvpbot path attack <name> <true/false>`| Kampfmodus umschalten |
| `/pvpbot path show <name> <true/false>`| Pfadvisualisierung umschalten |
| `/pvpbot path distribute <path>`| Bots gleichmäßig entlang des Pfades verteilen |
| `/pvpbot path startnear <path> <radius>`| Startpfad für Bots im Umkreis |
| `/pvpbot path stopall <path>`| Alle Bots auf diesem Pfad stoppen |

### Beispiele

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

Eine ausführliche Anleitung finden Sie auf der Seite [Pfade](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Paths).

---

## ⚙️ Einstellungen

Verwenden`/pvpbot settings`um alle aktuellen Einstellungen anzuzeigen.

Verwenden`/pvpbot settings <setting>`um den aktuellen Wert zu sehen.

Verwenden`/pvpbot settings <setting> <value>`um eine Einstellung zu ändern.

Verwenden`/pvpbot settings gui`um das grafische Einstellungsmenü zu öffnen.

Eine vollständige Liste aller Einstellungen finden Sie auf der Seite [Einstellungen](https://github.com/Stepan1411/pvp-bot-fabric/wiki/Settings).

### Schnelle Beispiele

```mcfunction
# Enable auto-targeting
/pvpbot settings autotarget true

# Set miss chance to 20%
/pvpbot settings misschance 20

# Enable bunny hop
/pvpbot settings bhop true
```
