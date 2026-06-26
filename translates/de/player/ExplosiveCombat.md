# 💥 Explosiver Kampf

Der PVP-Bot unterstützt fortgeschrittene explosive Kampftaktiken mithilfe von Endkristallen und Respawn-Ankern.

---

## 💎 Crystal PVP

Crystal PVP is a high-damage combat technique using End Crystals and Obsidian.

### Wie es funktioniert
1. Bot places obsidian near the target
2. Bot places End Crystal on the obsidian
3. Bot lässt den Kristall explodieren und verursacht massiven Explosionsschaden
4. Bot berechnet Sicherheitsabstände, um Selbstschäden zu vermeiden

### Kristall-PVP aktivieren
```mcfunction
/pvpbot settings crystalpvp true
```

### Anforderungen
Bots benötigen in ihrem Inventar:
- **Obsidian** - for crystal placement base
- **Endkristalle** – für Explosionen

### Taktik
- Bots halten einen Sicherheitsabstand zu Explosionen ein
- Automatische Kristallplatzierung und -detonation
- Funktioniert in allen Dimensionen
- Hoher Schadensausstoß (bis zu 20 Herzen)

---

## ⚓ Anker-PVP

Anchor PVP verwendet Respawn-Anker als Sprengwaffen in Overworld und End.

### Wie es funktioniert
1. Bot platziert Respawn-Anker in der Nähe des Ziels
2. Bot lädt den Anker mit Glowstone auf
3. Bot versucht, Spawn zu setzen (löst eine Explosion aus)
4. Massiver Schaden an nahegelegenen Einheiten

### Anker-PVP aktivieren
```mcfunction
/pvpbot settings anchorpvp true
```

### Anforderungen
Bots benötigen in ihrem Inventar:
- **Respawn-Anker** – der Sprengsatz
- **Glowstone** – um den Anker aufzuladen

### Important Notes
- Funktioniert nur in Overworld und End (nicht in Nether)
- In Nether funktionieren Anker normal (keine Explosion)
- Sehr hoher Schadensausstoß
- Consumes anchor and glowstone per use

---

## ⚙️ Einstellungen

| Einstellung | Geben Sie | ein Standard | Beschreibung |
|---------|------|---------|-------------|
| `crystalpvp` | bool | false | Enable Crystal PVP |
| `anchorpvp` | bool | false | Enable Anchor PVP |

---

## 💡 Nutzungstipps

### Kristall-PVP
- Geben Sie Bots Stapel von Obsidian und Kristallen
- Works best at medium range (5-10 blocks)
- Sehr effektiv gegen gepanzerte Gegner
- Kann Schilde durchbrechen

### Anker-PVP
- Teurer als Crystal PVP (verbraucht Anker bei jedem Gebrauch)
- Extrem hoher Schaden
- Am besten als Finishing-Move verwendet
- Füllen Sie Ihren Glowstone-Vorrat auf

### Taktiken kombinieren
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

## 🛡️ Sicherheit

Bots automatisch:
- Berechnen Sie sichere Explosionsabstände
- Vermeiden Sie nach Möglichkeit Selbstschäden
- Geben Sie dem Zielschaden Vorrang vor der Selbsterhaltung
- Benutzen Sie Totems der Unsterblichen, falls verfügbar

---

## 🔗 Verwandte Seiten

- [Kampfsystem](Combat.md) – Allgemeine Kampfmechanik
- [Einstellungen](Settings.md) – Alle Konfigurationsoptionen
– [Befehle](Commands.md) – Befehlsreferenz
