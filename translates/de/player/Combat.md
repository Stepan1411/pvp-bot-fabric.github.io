# ⚔️ Kampfsystem

PVP Bot verfügt über eine fortschrittliche Kampf-KI, die verschiedene Waffen und Taktiken einsetzen kann.

---

## 🗡️ Waffentypen

### Melee Combat
- **Schwerter** – Schnelle Angriffe, guter Schaden
- **Äxte** – Langsamer, kann aber Schilde brechen
- Bots automatically switch to melee when enemies are close

### Fernkampf
- **Bögen** – Pfeile ziehen und loslassen
- **Armbrüste** – Bolzen laden und abfeuern
- Bots halten optimalen Abstand (8-20 Blöcke)

### Streitkolbenkampf
- **Mace + Wind Charge** - Jump attacks for massive damage
- Bots nutzen Windladungen, um in die Luft zu fliegen
- Verheerende Sturzangriffe

### ElytraMace Combat
- **Elytra + Streitkolben + Feuerwerk** – Fortgeschrittene Luftangriffstechnik
- Bots rüsten Flügeldecken aus und nutzen Feuerwerk, um an Höhe zu gewinnen
- Entfernen Sie die Flügeldecken in der Luft und greifen Sie mit der Keule an, um massiven Fallschaden zu verursachen
- Waffenauswahl mit höchster Priorität, sofern verfügbar
- Konfigurierbare Höhen-, Distanz- und Wiederholungseinstellungen

### Kristall-PVP
- **Endkristalle + Obsidian** – Obsidian platzieren und Kristalle zur Detonation bringen
- Bots berechnen sichere Explosionsabstände
- Automatische Kristallplatzierung und -detonation
- Explosiver Kampf mit hohem Schaden

### Anker-PVP
- **Respawn-Anker + Leuchtstein** – Explosive Waffe in Overworld/End
- Bots laden Anker mit Leuchtsteinen auf
- Detonieren Sie und verursachen Sie massiven Schaden
- Funktioniert nur außerhalb des Nethers

---

## 🎯 Targeting

### Rachemodus
Wenn ein Bot Schaden erleidet, zielt er automatisch auf den Angreifer.
```mcfunction
/pvpbot settings revenge true
```

### Automatisches Ziel
Bots automatically search for enemies within view distance.
```mcfunction
/pvpbot settings autotarget true
```

### Manual Target
Zwingen Sie einen Bot, ein bestimmtes Ziel anzugreifen.
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

### Auto-Shield
Bots automatically raise shields when enemies attack.
```mcfunction
/pvpbot settings autoshield true
```

### Schild brechen
Bots verwenden Äxte, um feindliche Schilde zu deaktivieren.
```mcfunction
/pvpbot settings shieldbreak true
```

### Auto-Totem
Bots behalten Totems der Unsterblichen in der Nebenhand.
```mcfunction
/pvpbot settings autototem true
/pvpbot settings totempriority true  # Prioritize totem over shield
```

### Automatische Reparatur
Bots reparieren beschädigte Rüstungen automatisch mithilfe von XP-Flaschen.
```mcfunction
/pvpbot settings automend true
/pvpbot settings menddurability 0.5  # Repair at 50% durability
```

---

## 🍎 Heilung

### Auto-Essen
Bots fressen Nahrung, wenn:
- Gesundheit ist niedrig (< 30 %)
- Der Hunger liegt unter der Schwelle

```mcfunction
/pvpbot settings autoeat true
/pvpbot settings minhunger 14
```

### Auto-Tränke
Bots verwenden automatisch Tränke:
- **Heiltränke** – wenn die HP niedrig sind (Spritzer oder trinkbar)
- **Stärketränke** – beim Eintritt in den Kampf
- **Geschwindigkeitstränke** – beim Eintritt in den Kampf
- **Feuerwiderstandstränke** – beim Eintritt in den Kampf

Alle Buff-Tränke werden auf einmal gewürfelt, wenn der Kampf beginnt. Bots wenden Buffs erneut an, wenn die Effekte ablaufen (< 5 Sekunden verbleibend).

```mcfunction
/pvpbot settings autopotion true
```

### Rückzug
Wenn die Gesundheit niedrig ist, ziehen sich Bots zurück, während sie fressen/heilen.
Der Rückzug ist deaktiviert, wenn der Bot keine Nahrung hat (Kämpfe bis zum Tod).

```mcfunction
/pvpbot settings retreat true
/pvpbot settings retreathp 0.3  # 30% HP
```

---

## 💥 Kritische Treffer

Bots können kritische Treffer ausführen, indem sie ihre Angriffe mit Sprüngen zeitlich festlegen.
```mcfunction
/pvpbot settings criticals true
```

---

## 🕸️ Spinnennetz-Taktik

Bots können Spinnweben strategisch nutzen:
- **Beim Rückzug** – platziert ein Spinnennetz unter dem verfolgenden Feind, um ihn zu verlangsamen
- **Im Nahkampf** – platziert ein Spinnennetz unter dem angreifenden Feind

```mcfunction
/pvpbot settings cobweb true
```

---

## ⚙️ Kampfeinstellungen

| Einstellung | Reichweite | Standard | Beschreibung |
|---------|-------|---------|-------------|
| `combat`| wahr/falsch | wahr | Kampf aktivieren |
| `revenge`| wahr/falsch | wahr | Greife an, wer dich angegriffen hat |
| `autotarget`| wahr/falsch | falsch | Feinde automatisch finden |
| `criticals`| wahr/falsch | wahr | Kritische Treffer |
| `ranged`| wahr/falsch | wahr | Benutze Bögen |
| `mace`| wahr/falsch | wahr | Benutze Streitkolben |
| `spear`| wahr/falsch | falsch | Verwenden Sie Speer (Buggy) |
| `crystalpvp`| wahr/falsch | falsch | Verwenden Sie Kristall-PVP |
| `anchorpvp`| wahr/falsch | falsch | Verwenden Sie Anker-PVP |
| `elytramace`| wahr/falsch | wahr | Verwenden Sie den ElytraMace-Trick |
| `autopotion`| wahr/falsch | wahr | Tränke automatisch verwenden |
| `automend`| wahr/falsch | wahr | Autoreparatur-Rüstung |
| `menddurability`| 0,1-1,0 | 0,5 | Haltbarkeit % zu reparieren |
| `totempriority`| wahr/falsch | wahr | Totem über Schild |
| `cobweb`| wahr/falsch | wahr | Verwenden Sie Spinnweben |
| `retreat`| wahr/falsch | wahr | Rückzug bei niedrigen HP |
| `retreathp`| 0,1-0,9 | 0,3 | HP % zum Rückzug |
| `attackcooldown`| 1-40 | 10 | Ticks zwischen Anfällen |
| `meleerange`| 2-6 | 3,5 | Nahkampfangriffsdistanz |
| `viewdistance`| 5-128 | 64 | Zielsuchbereich |
