# 🚶 Navigationssystem

PVP Bot bietet intelligente Wegfindung, Bewegungsmechanik und erweiterte Bewegungsbefehle.

---

## 🎯 Bewegungsbefehle

### Folgen Sie dem System
Bots können Spielern oder anderen Bots folgen und dabei den optimalen Abstand wahren:

```mcfunction
# Make bot follow a target
/pvpbot follow Bot1 Steve

# Stop following
/pvpbot stopmovement Bot1
```

**Verhalten:**
- Hält einen Abstand von 3 Blocks zum Ziel ein
- Vermeidet automatisch Hindernisse
- Verfolgt das Ziel über alle Dimensionen hinweg
- Verwendet intelligente Wegfindung

### Begleitsystem
Verbesserter Verfolgungsmodus mit Verteidigungsmöglichkeiten:

```mcfunction
# Make bot escort (follow + protect) a target
/pvpbot escort Bot1 Steve
```

**Verhalten:**
- Identisch mit dem Folgemodus
- Verteidigt das Ziel automatisch, wenn es angegriffen wird
- Priorisiert den Zielschutz gegenüber anderen Kämpfen

### Gehe zum System
Direkte koordinatenbasierte Bewegung:

```mcfunction
# Send bot to specific coordinates
/pvpbot goto Bot1 100 64 200

# Enable Baritone for advanced pathfinding
/pvpbot settings gotousebaritone true
```

**Verhalten:**
- Intelligente Wegfindung zu Koordinaten
- Hindernisvermeidung und Springen
- Optionale Bariton-Integration für komplexe Pfade
- Funktioniert auf verschiedenen Geländetypen

---

## 🧭 Wegfindung

### Hindernisvermeidung
Bots erkennen und vermeiden automatisch:
- **Wände** - Biegen Sie links/rechts ab, um herumzugehen
- **Löcher** – Über Lücken springen
- **1-Block-Hindernisse** - Hochspringen

### Klettern
Bots können klettern:
- Leitern
- Reben
- Gerüste
- Sich windende/weinende Ranken

---

## 🐰 Bunny Hop (Bhop)

Bots können Bunny-Hop machen, um sich schneller fortzubewegen – sie springen, während sie sprinten, um die Geschwindigkeit zu steigern.

```mcfunction
# Enable/disable bhop
/pvpbot settings bhop true

# Set cooldown between jumps (5-30 ticks)
/pvpbot settings bhopcooldown 12

# Add extra jump height (0.0-0.5)
/pvpbot settings jumpboost 0.1
```

### Wenn Bhop aktiviert wird
- Geschwindigkeit ist >= 1,0
- Keine Hindernisse vor uns
- Nicht klettern
- Am Boden

---

## 😴 Müßiges Wandern

Wenn Bots kein Ziel haben, wandern sie um ihren Spawnpunkt herum.

```mcfunction
# Enable/disable idle wandering
/pvpbot settings idle true

# Set wander radius (3-50 blocks)
/pvpbot settings idleradius 10
```

### Verhalten
- Bots gehen langsam (nicht sprinten)
- Bleiben Sie im Umkreis des Spawnpunkts
- Wählen Sie zufällige Ziele
- Vermeiden Sie beim Wandern Hindernisse

---

## 🏃 Bewegungsgeschwindigkeiten

Unterschiedliche Situationen erfordern unterschiedliche Geschwindigkeiten:

| Situation | Geschwindigkeit | Bhop |
|-----------|-------|------|
| Müßiges Wandern | 0,5 | ❌ |
| Annäherung an das Ziel | 1,0 | ✅ |
| Essen (Zurückziehen) | 1.2 | ✅ |
| Rückzug bei niedrigem HP | 1,5 | ✅ |

---

## ⚙️ Navigationseinstellungen

| Einstellung | Reichweite | Standard | Beschreibung |
|---------|-------|---------|-------------|
| `bhop`| wahr/falsch | wahr | Bunny Hop aktivieren |
| `bhopcooldown`| 5-30 | 12 | Ticks zwischen Sprüngen |
| `jumpboost`| 0,0-0,5 | 0,0 | Zusätzliche Sprunghöhe |
| `idle`| wahr/falsch | wahr | Leerlauf aktivieren |
| `idleradius`| 3-50 | 10 | Wanderradius |
| `movespeed`| 0,1-2,0 | 1,0 | Grundbewegungsgeschwindigkeit |
| `gotousebaritone`| wahr/falsch | falsch | Verwenden Sie Bariton für goto |

---

## 🔧 Fehlerbehebung

### Bot bleibt hängen
- Bots versuchen automatisch, sich zu lösen
- Sie springen und ändern die Richtung, nachdem sie sich 10 Ticks lang nicht bewegt haben
- Wenn Sie immer noch nicht weiterkommen, versuchen Sie, den Bot zu teleportieren

### Bot klettert nicht
- Stellen Sie sicher, dass die Leiter/Ranke richtig platziert ist
- Der Bot muss dem kletterbaren Block zugewandt sein

### Bot fällt in Löcher
- Bots versuchen, über 2-Block-Lücken zu springen
- Größere Lücken können zu Stürzen führen
- Erwägen Sie den Bau von Brücken für wichtige Wege
