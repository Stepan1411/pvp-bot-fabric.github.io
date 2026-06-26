# ⚙️ Paramètres

Liste complète de toutes les options de configuration.

---

## 📋 Commandes

```mcfunction
# Show all settings
/pvpbot settings

# Show specific setting
/pvpbot settings <name>

# Change setting
/pvpbot settings <name> <value>
```

---

## ⚔️ Paramètres de combat

| Paramètre | Tapez | Gamme | Par défaut | Descriptif |
|---------|------|-------|---------|-------------|
| `combat`| booléen | - | vrai | Activer/désactiver le système de combat |
| `revenge`| booléen | - | vrai | Attaquez les entités qui endommagent le bot |
| `autotarget`| booléen | - | faux | Rechercher automatiquement les ennemis |
| `targetplayers`| booléen | - | vrai | Peut cibler les joueurs |
| `targetmobs`| booléen | - | faux | Peut cibler des foules hostiles |
| `targetbots`| booléen | - | faux | Peut cibler d'autres robots |
| `criticals`| booléen | - | vrai | Effectuer des coups critiques |
| `ranged`| booléen | - | vrai | Utiliser des arcs/arbalètes |
| `mace`| booléen | - | vrai | Utiliser une masse avec des charges de vent |
| `spear`| booléen | - | faux | Utiliser la lance (désactivée en raison d'un bug de tapis) |
| `crystalpvp`| booléen | - | faux | Utiliser du cristal PVP (obsidienne + cristaux) |
| `anchorpvp`| booléen | - | faux | Utiliser l'ancre PVP (ancre de réapparition + pierre lumineuse) |
| `elytramace`| booléen | - | vrai | Utiliser l'astuce ElytraMace (élytres + masse) |
| `attackcooldown`| entier | 1-40 | 10 | Tiques entre les attaques |
| `meleerange`| double | 2-6 | 3.5 | Distance d'attaque en mêlée |
| `movespeed`| double | 0,1-2,0 | 1.0 | Multiplicateur de vitesse de déplacement |
| `viewdistance`| double | 5-128 | 64 | Portée maximale de détection de cible |
| `retreat`| booléen | - | vrai | Retraite lorsque les PV sont faibles |
| `retreathp`| double | 0,1-0,9 | 0,3 | Pourcentage de HP pour commencer la retraite (30%) |

---

## 🧪 Paramètres des potions

| Paramètre | Tapez | Gamme | Par défaut | Descriptif |
|---------|------|-------|---------|-------------|
| `autopotion`| booléen | - | vrai | Potions de guérison/buff à utilisation automatique |
| `cobweb`| booléen | - | vrai | Utilisez des toiles d'araignées pour ralentir les ennemis |

Les robots utilisent automatiquement :
- **Potions de guérison** lorsque les PV sont faibles
- **Potions de force** en entrant en combat
- **Potions de vitesse** en entrant en combat
- **Potions de résistance au feu** en entrant en combat
- **Toiles d'araignées** pour ralentir les ennemis (lors de la retraite ou de la charge de l'ennemi)

Toutes les potions de buff sont lancées en même temps lorsque le combat commence ou lorsque les effets expirent.

---

## 🚶 Paramètres de navigation

| Paramètre | Tapez | Gamme | Par défaut | Descriptif |
|---------|------|-------|---------|-------------|
| `bhop`| booléen | - | vrai | Activer le lapin hop |
| `bhopcooldown`| entier | 5-30 | 12 | Tiques entre les sauts bhop |
| `jumpboost`| double | 0,0-0,5 | 0,0 | Hauteur de saut supplémentaire |
| `idle`| booléen | - | vrai | Promenez-vous quand aucune cible |
| `idleradius`| double | 3-50 | 10 | Rayon de dérapage au ralenti |

---

## 🛡️ Paramètres de l'équipement

| Paramètre | Tapez | Gamme | Par défaut | Descriptif |
|---------|------|-------|---------|-------------|
| `autoarmor`| booléen | - | vrai | Équiper automatiquement la meilleure armure |
| `autoweapon`| booléen | - | vrai | Équiper automatiquement la meilleure arme |
| `autototem`| booléen | - | vrai | Totem à équiper automatiquement en main levée |
| `totempriority`| booléen | - | vrai | Donner la priorité au totem plutôt qu'au bouclier |
| `autoshield`| booléen | - | vrai | Bouclier à utilisation automatique lors du blocage |
| `automend`| booléen | - | vrai | Armure de réparation automatique avec des bouteilles XP |
| `menddurability`| double | 0,1-1,0 | 0,5 | Seuil de % de durabilité à réparer (50%) |
| `prefersword`| booléen | - | vrai | Préférez l’épée à la hache |
| `shieldbreak`| booléen | - | vrai | Passez à la hache pour briser le bouclier ennemi |
| `droparmor`| booléen | - | faux | Lâchez des pièces d'armure pires |
| `dropweapon`| booléen | - | faux | Lâchez les pires armes |
| `dropdistance`| double | 1-10 | 3.0 | Distance de retrait des articles |
| `interval`| entier | 1-100 | 20 | Intervalle de contrôle de l'équipement (tiques) |
| `minarmorlevel`| entier | 0-100 | 0 | Niveau d'armure minimum pour équiper |

### Niveaux d'armure
| Niveau | Type d'armure |
|-------|------------|
| 0 | N'importe quelle armure |
| 20 | Cuir+ |
| 40 | Or+ |
| 50 | Chaîne+ |
| 60 | Fer+ |
| 80 | Diamant+ |
| 100 | Netherite uniquement |

---

## 🎭 Paramètres de réalisme

| Paramètre | Tapez | Gamme | Par défaut | Descriptif |
|---------|------|-------|---------|-------------|
| `misschance`| entier | 0-100 | 10 | Chance de rater des attaques (%) |
| `mistakechance`| entier | 0-100 | 5 | Chance d'attaquer dans la mauvaise direction (%) |
| `reactiondelay`| entier | 0-20 | 0 | Délai avant de réagir (tiques) |

---

## 👥 Autres paramètres

| Paramètre | Tapez | Gamme | Par défaut | Descriptif |
|---------|------|-------|---------|-------------|
| `factions`| booléen | - | vrai | Activer le système de faction |
| `friendlyfire`| booléen | - | faux | Autoriser les dégâts aux alliés de la faction |
| `specialnames`| booléen | - | faux | Utiliser des noms spéciaux de la base de données |
| `gotousebaritone`| booléen | - | faux | Utiliser Baryton pour les commandes goto |

---

## 🚀 Paramètres ElytraMace

| Paramètre | Tapez | Gamme | Par défaut | Descriptif |
|---------|------|-------|---------|-------------|
| `elytramace`| booléen | - | vrai | Activer l'astuce ElytraMace |
| `elytramaceretries`| entier | 1-10 | 1 | Nombre maximal de tentatives de décollage |
| `elytramacealtitude`| entier | 5-50 | 20 | Altitude minimale pour l'attaque |
| `elytramacedistance`| double | 3-15 | 8.0 | Distance d'attaque de la cible |
| `elytramacefireworks`| entier | 1-10 | 3 | Nombre de feux d'artifice à utiliser |

**ElytraMace Trick :** Le robot équipe les élytres, utilise des feux d'artifice pour voler, supprime les élytres dans les airs et attaque avec une masse pour infliger d'énormes dégâts de chute.

---

## 💾 Fichiers de configuration

Les paramètres sont enregistrés dans :
```
config/pvp_bot.json
```

Les données du bot (positions, dimensions, modes de jeu) sont enregistrées dans :
```
config/pvp_bot_bots.json
```

Les paramètres et les robots persistent lors des redémarrages du serveur. Les robots sont automatiquement restaurés au démarrage du serveur.

---

## 📋 Exemples

### Rendre les robots plus réalistes
```mcfunction
/pvpbot settings misschance 15
/pvpbot settings mistakechance 10
/pvpbot settings reactiondelay 5
```

### Rendre les robots agressifs
```mcfunction
/pvpbot settings autotarget true
/pvpbot settings targetplayers true
/pvpbot settings targetbots true
/pvpbot settings revenge true
```

### Désactiver le combat à distance
```mcfunction
/pvpbot settings ranged false
/pvpbot settings mace false
/pvpbot settings crystalpvp false
/pvpbot settings anchorpvp false
```

### Mouvement rapide
```mcfunction
/pvpbot settings bhop true
/pvpbot settings bhopcooldown 8
/pvpbot settings jumpboost 0.2
/pvpbot settings movespeed 1.5
```

### Gardes fixes
```mcfunction
/pvpbot settings idle false
/pvpbot settings bhop false
```

### Activer l'astuce ElytraMace
```mcfunction
/pvpbot settings elytramace true
/pvpbot settings elytramacealtitude 25
/pvpbot settings elytramaceretries 2
```

### Activer les commandes de mouvement avec Baryton
```mcfunction
/pvpbot settings gotousebaritone true
```

### Activer les noms spéciaux
```mcfunction
/pvpbot settings specialnames true
```
