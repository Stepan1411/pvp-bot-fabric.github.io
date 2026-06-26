# ⚙️ Einstellungen

Vollständige Liste aller Konfigurationsoptionen.

---

## 📋 Befehle

```mcfunction
# Show all settings
/pvpbot settings

# Show specific setting
/pvpbot settings <name>

# Change setting
/pvpbot settings <name> <value>
```

---

## ⚔️ Kampfeinstellungen

| Einstellung | Geben Sie | ein Reichweite | Standard | Beschreibung |
|---------|------|-------|---------|-------------|
| `combat`| bool | - | wahr | Kampfsystem aktivieren/deaktivieren |
| `revenge`| bool | - | wahr | Angriffseinheiten, die dem Bot Schaden zufügen |
| `autotarget`| bool | - | falsch | Automatisch nach Feinden suchen |
| `targetplayers`| bool | - | wahr | Kann auf Spieler abzielen |
| `targetmobs`| bool | - | falsch | Kann feindliche Mobs angreifen |
| `targetbots`| bool | - | falsch | Kann andere Bots angreifen |
| `criticals`| bool | - | wahr | Kritische Treffer ausführen |
| `ranged`| bool | - | wahr | Benutze Bögen/Armbrüste |
| `mace`| bool | - | wahr | Benutze Streitkolben mit Windladungen |
| `spear`| bool | - | falsch | Speer verwenden (wegen Teppichfehler deaktiviert) |
| `crystalpvp`| bool | - | falsch | Verwenden Sie Kristall-PVP (Obsidian + Kristalle) |
| `anchorpvp`| bool | - | falsch | Benutze Anker-PVP (Respawn-Anker + Leuchtstein) |
| `elytramace`| bool | - | wahr | Benutze den ElytraMace-Trick (Elytra + Keule) |
| `attackcooldown`| int | 1-40 | 10 | Ticks zwischen Anfällen |
| `meleerange`| doppelt | 2-6 | 3,5 | Nahkampfangriffsdistanz |
| `movespeed`| doppelt | 0,1-2,0 | 1,0 | Bewegungsgeschwindigkeitsmultiplikator |
| `viewdistance`| doppelt | 5-128 | 64 | Maximale Zielerfassungsreichweite |
| `retreat`| bool | - | wahr | Rückzug bei niedrigen HP |
| `retreathp`| doppelt | 0,1-0,9 | 0,3 | HP-Prozent zum Beginn des Rückzugs (30 %) |

---

## 🧪 Trankeinstellungen

| Einstellung | Geben Sie | ein Reichweite | Standard | Beschreibung |
|---------|------|-------|---------|-------------|
| `autopotion`| bool | - | wahr | Heil-/Buff-Tränke automatisch verwenden |
| `cobweb`| bool | - | wahr | Verwenden Sie Spinnweben, um Feinde zu verlangsamen |

Bots verwenden automatisch:
- **Heiltränke**, wenn die HP niedrig sind
- **Stärketränke** beim Eintritt in den Kampf
- **Geschwindigkeitstränke** beim Eintritt in den Kampf
- **Feuerwiderstandstränke** beim Eintritt in den Kampf
- **Spinnenweben**, um Feinde zu verlangsamen (beim Rückzug oder beim Angriff des Feindes)

Alle Buff-Tränke werden auf einmal ausgegeben, wenn der Kampf beginnt oder wenn die Effekte ablaufen.

---

## 🚶 Navigationseinstellungen

| Einstellung | Geben Sie | ein Reichweite | Standard | Beschreibung |
|---------|------|-------|---------|-------------|
| `bhop`| bool | - | wahr | Bunny Hop aktivieren |
| `bhopcooldown`| int | 5-30 | 12 | Ticks zwischen Bhop-Sprüngen |
| `jumpboost`| doppelt | 0,0-0,5 | 0,0 | Zusätzliche Sprunghöhe |
| `idle`| bool | - | wahr | Wandern, wenn kein Ziel |
| `idleradius`| doppelt | 3-50 | 10 | Leerlaufradius |

---

## 🛡️ Geräteeinstellungen

| Einstellung | Geben Sie | ein Reichweite | Standard | Beschreibung |
|---------|------|-------|---------|-------------|
| `autoarmor`| bool | - | wahr | Beste Rüstung automatisch ausrüsten |
| `autoweapon`| bool | - | wahr | Beste Waffe automatisch ausrüsten |
| `autototem`| bool | - | wahr | Totem automatisch in der Nebenhand ausrüsten |
| `totempriority`| bool | - | wahr | Priorisieren Sie Totem vor Schild |
| `autoshield`| bool | - | wahr | Schild beim Blockieren automatisch verwenden |
| `automend`| bool | - | wahr | Automatische Reparatur von Rüstungen mit XP-Flaschen |
| `menddurability`| doppelt | 0,1-1,0 | 0,5 | Haltbarkeit % Reparaturschwelle (50 %) |
| `prefersword`| bool | - | wahr | Lieber Schwert als Axt |
| `shieldbreak`| bool | - | wahr | Wechseln Sie zur Axt, um den gegnerischen Schild zu durchbrechen |
| `droparmor`| bool | - | falsch | Schlechtere Rüstungsteile fallen lassen |
| `dropweapon`| bool | - | falsch | Schlimmere Waffen fallen lassen |
| `dropdistance`| doppelt | 1-10 | 3,0 | Artikelabholentfernung |
| `interval`| int | 1-100 | 20 | Geräteprüfintervall (Ticks) |
| `minarmorlevel`| int | 0-100 | 0 | Mindestrüstungsstufe zum Ausrüsten |

### Rüstungsstufen
| Ebene | Rüstungstyp |
|-------|------------|
| 0 | Jede Rüstung |
| 20 | Leder+ |
| 40 | Gold+ |
| 50 | Kette+ |
| 60 | Eisen+ |
| 80 | Diamant+ |
| 100 | Nur Netherit |

---

## 🎭 Realismus-Einstellungen

| Einstellung | Geben Sie | ein Reichweite | Standard | Beschreibung |
|---------|------|-------|---------|-------------|
| `misschance`| int | 0-100 | 10 | Chance, Angriffe zu verpassen (%) |
| `mistakechance`| int | 0-100 | 5 | Chance, in die falsche Richtung anzugreifen (%) |
| `reactiondelay`| int | 0-20 | 0 | Verzögerung bis zur Reaktion (Ticks) |

---

## 👥 Andere Einstellungen

| Einstellung | Geben Sie | ein Reichweite | Standard | Beschreibung |
|---------|------|-------|---------|-------------|
| `factions`| bool | - | wahr | Fraktionssystem aktivieren |
| `friendlyfire`| bool | - | falsch | Schaden an Fraktionsverbündeten zulassen |
| `specialnames`| bool | - | falsch | Verwenden Sie spezielle Namen aus der Datenbank |
| `gotousebaritone`| bool | - | falsch | Verwenden Sie Bariton für Gehe zu-Befehle |

---

## 🚀 ElytraMace-Einstellungen

| Einstellung | Geben Sie | ein Reichweite | Standard | Beschreibung |
|---------|------|-------|---------|-------------|
| `elytramace`| bool | - | wahr | ElytraMace-Trick aktivieren |
| `elytramaceretries`| int | 1-10 | 1 | Max. Startwiederholungsversuche |
| `elytramacealtitude`| int | 5-50 | 20 | Mindesthöhe für Angriff |
| `elytramacedistance`| doppelt | 3-15 | 8,0 | Angriffsentfernung vom Ziel |
| `elytramacefireworks`| int | 1-10 | 3 | Anzahl der zu verwendenden Feuerwerkskörper |

**ElytraMace-Trick:** Bot rüstet Elytra aus, fliegt mit Feuerwerkskörpern hoch, entfernt Elytra in der Luft und greift mit Streitkolben an, um massiven Fallschaden zu verursachen.

---

## 💾 Konfigurationsdateien

Einstellungen werden gespeichert in:
```
config/pvp_bot.json
```

Bot-Daten (Positionen, Abmessungen, Spielmodi) werden gespeichert in:
```
config/pvp_bot_bots.json
```

Sowohl die Einstellungen als auch die Bots bleiben bei Serverneustarts bestehen. Bots werden automatisch wiederhergestellt, wenn der Server startet.

---

## 📋 Beispiele

### Machen Sie Bots realistischer
```mcfunction
/pvpbot settings misschance 15
/pvpbot settings mistakechance 10
/pvpbot settings reactiondelay 5
```

### Machen Sie Bots aggressiv
```mcfunction
/pvpbot settings autotarget true
/pvpbot settings targetplayers true
/pvpbot settings targetbots true
/pvpbot settings revenge true
```

### Fernkampf deaktivieren
```mcfunction
/pvpbot settings ranged false
/pvpbot settings mace false
/pvpbot settings crystalpvp false
/pvpbot settings anchorpvp false
```

### Schnelle Bewegung
```mcfunction
/pvpbot settings bhop true
/pvpbot settings bhopcooldown 8
/pvpbot settings jumpboost 0.2
/pvpbot settings movespeed 1.5
```

### Stationäre Wachen
```mcfunction
/pvpbot settings idle false
/pvpbot settings bhop false
```

### Aktivieren Sie den ElytraMace-Trick
```mcfunction
/pvpbot settings elytramace true
/pvpbot settings elytramacealtitude 25
/pvpbot settings elytramaceretries 2
```

### Bewegungsbefehle mit Bariton aktivieren
```mcfunction
/pvpbot settings gotousebaritone true
```

### Spezielle Namen aktivieren
```mcfunction
/pvpbot settings specialnames true
```
