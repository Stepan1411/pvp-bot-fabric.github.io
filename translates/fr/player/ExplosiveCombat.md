# 💥 Combat explosif

PVP Bot prend en charge les tactiques de combat explosives avancées utilisant End Crystals et Respawn Anchors.

---

## 💎 Cristal PVP

Crystal PVP est une technique de combat à dégâts élevés utilisant End Crystals et Obsidian.

### Comment ça marche
1. Le robot place l'obsidienne près de la cible
2. Bot places End Crystal on the obsidian
3. Le robot fait exploser le cristal pour provoquer d'énormes dégâts d'explosion
4. Le robot calcule les distances de sécurité pour éviter de s'automutiler

### Activer le PVP Cristal
```mcfunction
/pvpbot settings crystalpvp true
```

### Exigences
Les robots ont besoin dans leur inventaire :
- **Obsidian** - for crystal placement base
- **Cristaux de fin** - pour les explosions

### Tactiques
- Les robots maintiennent une distance de sécurité par rapport aux explosions
- Placement et détonation automatiques des cristaux
- Fonctionne dans toutes les dimensions
- Dégâts élevés (jusqu'à 20 cœurs)

---

## ⚓ Ancre PVP

Anchor PVP utilise les Respawn Anchors comme armes explosives dans Overworld et End.

### Comment ça marche
1. Le robot place l'ancre Respawn près de la cible
2. Le robot charge l'ancre avec Glowstone
3. Le robot tente de définir l'apparition (déclenche une explosion)
4. Dommages massifs aux entités voisines

### Activer le PVP d'ancrage
```mcfunction
/pvpbot settings anchorpvp true
```

### Exigences
Les robots ont besoin dans leur inventaire :
- **Respawn Anchor** - l'engin explosif
- **Glowstone** - pour charger l'ancre

### Remarques importantes
- Fonctionne uniquement dans Overworld et End (pas dans Nether)
- Dans le Nether, les ancres fonctionnent normalement (pas d'explosion)
- Dégâts très élevés
- Consumes anchor and glowstone per use

---

## ⚙️ Paramètres

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `crystalpvp` | bool | false | Enable Crystal PVP |
| `anchorpvp` | bool | false | Enable Anchor PVP |

---

## 💡 Conseils d'utilisation

### Cristal PvP
- Donnez aux robots des piles d'obsidienne et de cristaux
- Works best at medium range (5-10 blocks)
- Très efficace contre les adversaires blindés
- Peut briser les boucliers

### Ancre PVP
- Plus cher que Crystal PVP (consomme de l'ancre à chaque utilisation)
- Dégâts extrêmement élevés
- Mieux utilisé comme coup de finition
- Faites le plein de pierres lumineuses

### Combiner des tactiques
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

## 🛡️ Sécurité

Bots automatiquement :
- Calculer les distances d'explosion sûres
- Évitez de vous automutiler lorsque cela est possible
- Donner la priorité aux dégâts ciblés plutôt qu'à l'auto-préservation
- Utilisez des totems d'immortalité si disponibles

---

## 🔗 Pages connexes

- [Système de combat](Combat.md) - Mécanique générale de combat
- [Paramètres](Settings.md) - Toutes les options de configuration
- [Commands](Commands.md) - Référence des commandes
