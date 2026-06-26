# ⚔️ Système de combat

PVP Bot dispose d'une IA de combat avancée qui peut utiliser différentes armes et tactiques.

---

## 🗡️ Types d'armes

### Melee Combat
- **Épées** - Attaques rapides, bons dégâts
- **Haches** - Plus lentes mais peuvent briser les boucliers
- Bots automatically switch to melee when enemies are close

### Combat à distance
- **Arcs** - Dessinez et relâchez les flèches
- **Arbalètes** - Chargement et carreaux de tir
- Les robots gardent une distance optimale (8 à 20 blocs)

### Combat à la masse
- **Mace + Wind Charge** - Jump attacks for massive damage
- Les robots utilisent des charges de vent pour se lancer dans les airs
- Attaques de chute dévastatrices

### Combat d'ElytraMace
- **Elytra + Mace + Fireworks** - Technique d'attaque aérienne avancée
- Les robots équipent les élytres, utilisent des feux d'artifice pour prendre de l'altitude
- Supprimez les élytres dans les airs et attaquez avec la masse pour infliger des dégâts de chute massifs
- Sélection d'armes la plus prioritaire lorsqu'elle est disponible
- Paramètres configurables d'altitude, de distance et de nouvelle tentative

### Cristal PvP
- **Cristaux de fin + Obsidienne** - Placez l'obsidienne et faites exploser les cristaux
- Les robots calculent les distances d'explosion sûres
- Placement et détonation automatiques des cristaux
- Combat explosif à dégâts élevés

### Ancre PVP
- **Respawn Anchor + Glowstone** - Arme explosive dans Overworld/End
- Les robots chargent les ancres avec de la pierre lumineuse
- Exploser pour des dégâts massifs
- Fonctionne uniquement en dehors du Nether

---

## 🎯 Ciblage

### Mode Vengeance
Lorsqu'un robot subit des dégâts, il cible automatiquement l'attaquant.
```mcfunction
/pvpbot settings revenge true
```

### Auto-Target
Bots automatically search for enemies within view distance.
```mcfunction
/pvpbot settings autotarget true
```

### Cible manuelle
Force a bot to attack a specific target.
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
Les robots lèvent automatiquement leurs boucliers lorsque les ennemis attaquent.
```mcfunction
/pvpbot settings autoshield true
```

### Briser le bouclier
Les robots utilisent des haches pour désactiver les boucliers ennemis.
```mcfunction
/pvpbot settings shieldbreak true
```

### Auto-Totem
Les robots gardent les totems éternels à portée de main.
```mcfunction
/pvpbot settings autototem true
/pvpbot settings totempriority true  # Prioritize totem over shield
```

### Réparation automatique
Les robots réparent automatiquement les armures endommagées à l'aide de bouteilles XP.
```mcfunction
/pvpbot settings automend true
/pvpbot settings menddurability 0.5  # Repair at 50% durability
```

---

## 🍎 Guérison

### Manger automatiquement
Les robots mangent de la nourriture quand :
- La santé est faible (< 30%)
- La faim est en dessous du seuil

```mcfunction
/pvpbot settings autoeat true
/pvpbot settings minhunger 14
```

### Potions automatiques
Les robots utilisent automatiquement des potions :
- **Potions de guérison** - lorsque les HP sont faibles (splash ou buvable)
- **Potions de force** - lors de l'entrée en combat
- **Potions de vitesse** - lors de l'entrée en combat
- **Potions de résistance au feu** - en entrant en combat

Toutes les potions de buff sont lancées en même temps lorsque le combat commence. Les robots réappliquent les buffs lorsque les effets expirent (< 5 secondes restantes).

```mcfunction
/pvpbot settings autopotion true
```

### Retraite
Lorsque la santé est faible, les robots reculent tout en mangeant/soignant.
La retraite est désactivée si le bot n'a pas de nourriture (se bat jusqu'à la mort).

```mcfunction
/pvpbot settings retreat true
/pvpbot settings retreathp 0.3  # 30% HP
```

---

## 💥 Coups critiques

Les robots peuvent effectuer des coups critiques en chronométrant leurs attaques avec des sauts.
```mcfunction
/pvpbot settings criticals true
```

---

## 🕸️ Tactiques de toile d'araignée

Les robots peuvent utiliser les toiles d'araignées de manière stratégique :
- **Lors de la retraite** - place une toile d'araignée sous la poursuite de l'ennemi pour le ralentir
- **En combat au corps à corps** - place la toile d'araignée sous l'ennemi en charge

```mcfunction
/pvpbot settings cobweb true
```

---

## ⚙️ Paramètres de combat

| Paramètre | Gamme | Par défaut | Descriptif |
|---------|-------|---------|-------------|
| `combat`| vrai/faux | vrai | Activer le combat |
| `revenge`| vrai/faux | vrai | Attaque qui vous a attaqué |
| `autotarget`| vrai/faux | faux | Recherche automatique des ennemis |
| `criticals`| vrai/faux | vrai | Coups critiques |
| `ranged`| vrai/faux | vrai | Utilisez des arcs |
| `mace`| vrai/faux | vrai | Utiliser la masse |
| `spear`| vrai/faux | faux | Utiliser la lance (buggy) |
| `crystalpvp`| vrai/faux | faux | Utiliser du cristal PVP |
| `anchorpvp`| vrai/faux | faux | Utiliser l'ancre PVP |
| `elytramace`| vrai/faux | vrai | Utilisez l'astuce ElytraMace |
| `autopotion`| vrai/faux | vrai | Potions à usage automatique |
| `automend`| vrai/faux | vrai | Armure de réparation automatique |
| `menddurability`| 0,1-1,0 | 0,5 | Durabilité % à réparer |
| `totempriority`| vrai/faux | vrai | Totem sur bouclier |
| `cobweb`| vrai/faux | vrai | Utiliser des toiles d'araignées |
| `retreat`| vrai/faux | vrai | Retraite lorsque les PV sont faibles |
| `retreathp`| 0,1-0,9 | 0,3 | % de PV à battre en retraite |
| `attackcooldown`| 1-40 | 10 | Tiques entre les attaques |
| `meleerange`| 2-6 | 3.5 | Distance d'attaque en mêlée |
| `viewdistance`| 5-128 | 64 | Plage de recherche cible |
