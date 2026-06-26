# 🚶 Bewegungssystem

PVP Bot features an advanced movement system that allows bots to follow players, escort targets, and navigate to specific coordinates.

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

**Verhalten:**
- Hält einen Abstand von 3 Blocks zum Ziel ein
- Vermeidet automatisch Hindernisse
- Follows across dimensions
- Verwendet intelligente Wegfindung
– Stoppt, wenn das Ziel offline ist

### Begleitmodus
Verbesserter Verfolgungsmodus mit Verteidigungsfähigkeiten.

```mcfunction
# Make bot escort a player
/pvpbot escort Bot1 Steve

# Make bot escort another bot
/pvpbot escort Bot1 Bot2
```

**Verhalten:**
- Identisch mit dem Folgemodus
- **Verteidigt das Ziel automatisch**, wenn es angegriffen wird
- Priorisiert den Zielschutz gegenüber anderen Kämpfen
– Greift jeden an, der dem eskortierten Ziel Schaden zufügt

### Gehe zum Modus
Direkte koordinatenbasierte Bewegung.

```mcfunction
# Send bot to coordinates
/pvpbot goto Bot1 100 64 200

# Use relative coordinates
/pvpbot goto Bot1 ~10 ~ ~-5
```

**Verhalten:**
- Intelligente Wegfindung zu Koordinaten
- Hindernisvermeidung und Springen
- Optionale Bariton-Integration
- Stoppt, wenn das Ziel erreicht ist

---

## 🛑 Bewegung stoppen

```mcfunction
# Stop any movement mode
/pvpbot stopmovement Bot1
```

Dieser Befehl stoppt:
- Folgemodus
- Begleitmodus
- Gehe zum Modus
- Pfadverfolgung

---

## 👥 Fraktionsbewegung

Alle Bewegungsbefehle funktionieren mit Fraktionen:

```mcfunction
# Make entire faction follow a target
/pvpbot faction follow RedTeam Steve

# Make entire faction escort a target
/pvpbot faction escort RedTeam Steve

# Move entire faction to coordinates
/pvpbot faction goto RedTeam 100 64 200
```

---

## ⚙️ Bewegungseinstellungen

| Einstellung | Geben Sie | ein Reichweite | Standard | Beschreibung |
|---------|------|-------|---------|-------------|
| `movespeed`| doppelt | 0,1-2,0 | 1,0 | Grundbewegungsgeschwindigkeit |
| `bhop`| bool | - | wahr | Bunny Hop aktivieren |
| `bhopcooldown`| int | 5-30 | 12 | Ticks zwischen Sprüngen |
| `jumpboost`| doppelt | 0,0-0,5 | 0,0 | Zusätzliche Sprunghöhe |
| `gotousebaritone`| bool | - | falsch | Verwenden Sie Bariton für goto |

---

## 🧭 Bariton-Integration

Aktivieren Sie Bariton für erweiterte Wegfindung:

```mcfunction
/pvpbot settings gotousebaritone true
```

**Vorteile:**
- Komplexe Geländenavigation
- Wegfindung über große Entfernungen
- Automatischer Brückenbau
- Abbau durch Hindernisse

**Anforderungen:**
- Der Bariton-Mod muss installiert sein
- Funktioniert nur mit goto-Befehlen
- Möglicherweise langsamer als die einfache Wegfindung

---

## 🔧 Technische Details

### Abstand verfolgen
- **Zielentfernung:** 3 Blöcke
- **Stoppentfernung:** 2 Blocks
- **Maximale Distanz:** 50 Blöcke (bei Überschreitung teleportieren)

### Aktualisierungshäufigkeit
- Bewegungsaktualisierungen bei jedem Tick (20 Mal pro Sekunde)
- Zielposition alle 5 Ticks überprüft
- Die Wegfindung wird bei Bedarf neu berechnet

### Hindernisbewältigung
- Automatisches Springen über 1-Block-Hindernisse
- Wegfindung um Mauern und Barrieren herum
- Durch Wasser schwimmen
- Kletterleitern und Kletterpflanzen

---

## 🚨 Fehlerbehebung

### Bot folgt nicht
- Überprüfen Sie, ob das Ziel existiert und online ist
- Stellen Sie sicher, dass der Bot nicht hängen bleibt oder blockiert ist
- Stellen Sie sicher, dass die Bewegung nicht behindert ist
- Überprüfen Sie, ob sich der Bot im Kampf befindet (kann die Bewegung überschreiben)

### Bot bleibt hängen
- Verwenden`/pvpbot stopmovement`und neu starten
- Aktivieren Sie Bariton für komplexes Gelände
- Überprüfen Sie, ob Hindernisse den Weg blockieren
- Bot teleportieren, um den Bereich zu räumen

### Escort verteidigt nicht
- Überprüfen Sie, ob der Escort-Modus aktiv ist (nicht nur folgen).
- Überprüfen Sie, ob Friendly Fire deaktiviert ist
- Stellen Sie sicher, dass der Bot Waffen und Kampf aktiviert hat
– Das Ziel muss tatsächlich Schaden erleiden, um eine Verteidigung auszulösen

---

## 💡 Nutzungstipps

### Effektives Folgen
- Für beste Ergebnisse in offenen Bereichen verwenden
- Vermeiden Sie überfülltes oder komplexes Gelände
- Halten Sie Ziele mit angemessener Geschwindigkeit in Bewegung
- Benutzen Sie Begleitpersonen für wichtige Spieler

### Koordinatennavigation
- Use goto for precise positioning
- Aktivieren Sie Bariton für große Entfernungen
- Überprüfen Sie, ob die Koordinaten zugänglich sind
- Verwenden Sie relative Koordinaten für Bewegungen in der Nähe

### Fraktionskoordination
- Organisieren Sie große Gruppen mit Fraktionskommandos
- Nutzen Sie eine Begleitperson zum VIP-Schutz
- Koordinieren Sie Angriffe mit der Fraktion goto
- Verteilen Sie die Ankunft mit gestaffelten Befehlen