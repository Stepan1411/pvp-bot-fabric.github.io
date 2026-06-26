# 🚶 Système de navigation

PVP Bot propose une recherche de chemin intelligente, une mécanique de mouvement et des commandes de mouvement avancées.

---

## 🎯 Commandes de mouvement

### Suivre le système
Les robots peuvent suivre des joueurs ou d'autres robots tout en maintenant une distance optimale :

```mcfunction
# Make bot follow a target
/pvpbot follow Bot1 Steve

# Stop following
/pvpbot stopmovement Bot1
```

**Comportement:**
- Maintient une distance de 3 pâtés de maisons de la cible
- Évite automatiquement les obstacles
- Suit la cible dans toutes les dimensions
- Utilise une recherche de chemin intelligente

### Système d'escorte
Mode de suivi amélioré avec des capacités défensives :

```mcfunction
# Make bot escort (follow + protect) a target
/pvpbot escort Bot1 Steve
```

**Comportement:**
- Identique au mode suivi
- Défend automatiquement la cible en cas d'attaque
- Donne la priorité à la protection de la cible par rapport aux autres combats

### Aller au système
Mouvement direct basé sur les coordonnées :

```mcfunction
# Send bot to specific coordinates
/pvpbot goto Bot1 100 64 200

# Enable Baritone for advanced pathfinding
/pvpbot settings gotousebaritone true
```

**Comportement:**
- Recherche de chemin intelligente vers les coordonnées
- Évitement d'obstacles et saut
- Intégration baryton en option pour les chemins complexes
- Fonctionne sur différents types de terrain

---

## 🧭 Orientation

### Évitement d'obstacles
Les robots détectent et évitent automatiquement :
- **Murs** - Tourner à gauche/droite pour faire le tour
- **Trous** - Sauter par-dessus les espaces
- **Obstacles à 1 bloc** - Sauter

### Escalade
Les robots peuvent grimper :
- Échelles
- Vignes
- Échafaudage
- Vignes tordues/pleureuses

---

## 🐰 Lapin Hop (Bhop)

Les robots peuvent sauter en lapin pour des mouvements plus rapides – sauter tout en sprintant pour augmenter leur vitesse.

```mcfunction
# Enable/disable bhop
/pvpbot settings bhop true

# Set cooldown between jumps (5-30 ticks)
/pvpbot settings bhopcooldown 12

# Add extra jump height (0.0-0.5)
/pvpbot settings jumpboost 0.1
```

### Quand Bhop s'active
- La vitesse est >= 1,0
- Aucun obstacle à venir
- Ne pas grimper
- Au sol

---

## 😴 Errance inactive

Lorsque les robots n’ont pas de cible, ils errent autour de leur point d’apparition.

```mcfunction
# Enable/disable idle wandering
/pvpbot settings idle true

# Set wander radius (3-50 blocks)
/pvpbot settings idleradius 10
```

### Comportement
- Les robots marchent lentement (pas de sprint)
- Restez dans le rayon du point d'apparition
- Choisissez des destinations aléatoires
- Évitez les obstacles en errant

---

## 🏃 Vitesses de déplacement

Différentes situations utilisent des vitesses différentes :

| Situation | Vitesse | Bhop |
|---------------|-------|------|
| Errance oisive | 0,5 | ❌ |
| Objectif en approche | 1.0 | ✅ |
| Manger (se retirer) | 1.2 | ✅ |
| Retraite à faible HP | 1.5 | ✅ |

---

## ⚙️ Paramètres de navigation

| Paramètre | Gamme | Par défaut | Descriptif |
|---------|-------|---------|-------------|
| `bhop`| vrai/faux | vrai | Activer le lapin hop |
| `bhopcooldown`| 5-30 | 12 | Tiques entre les sauts |
| `jumpboost`| 0,0-0,5 | 0,0 | Hauteur de saut supplémentaire |
| `idle`| vrai/faux | vrai | Activer l'errance inactive |
| `idleradius`| 3-50 | 10 | Rayon d'errance |
| `movespeed`| 0,1-2,0 | 1.0 | Vitesse de déplacement de base |
| `gotousebaritone`| vrai/faux | faux | Utilisez Baryton pour aller à |

---

## 🔧 Dépannage

### Le robot reste bloqué
- Les robots essaient automatiquement de se décoller
- Ils sautent et changent de direction après 10 ticks sans mouvement
- Si toujours bloqué, essayez de téléporter le bot

### Le robot ne grimpe pas
- Assurez-vous que l'échelle/vigne est correctement placée
- Le bot doit être face au bloc grimpable

### Le robot tombe dans des trous
- Les robots tentent de sauter par-dessus des espaces de 2 blocs
- Des espaces plus grands peuvent provoquer des chutes
- Envisagez de construire des ponts pour les chemins importants
