# 🚶 Movement System

PVP Bot propose un système de mouvement avancé qui permet aux robots de suivre les joueurs, d'escorter des cibles et de naviguer vers des coordonnées spécifiques.

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

**Behavior:**
- Maintient une distance de 3 pâtés de maisons de la cible
- Évite automatiquement les obstacles
- Suit à travers les dimensions
- Uses smart pathfinding
- S'arrête lorsque la cible est hors ligne

### Mode Escorte
Mode de suivi amélioré avec des capacités défensives.

```mcfunction
# Make bot escort a player
/pvpbot escort Bot1 Steve

# Make bot escort another bot
/pvpbot escort Bot1 Bot2
```

**Comportement:**
- Identique au mode suivi
- **Défend automatiquement la cible** en cas d'attaque
- Donne la priorité à la protection de la cible par rapport aux autres combats
- Attaque quiconque endommage la cible escortée

### Passer au mode
Mouvement direct basé sur les coordonnées.

```mcfunction
# Send bot to coordinates
/pvpbot goto Bot1 100 64 200

# Use relative coordinates
/pvpbot goto Bot1 ~10 ~ ~-5
```

**Comportement:**
- Recherche de chemin intelligente vers les coordonnées
- Évitement d'obstacles et saut
- Intégration baryton en option
- S'arrête lorsque la destination est atteinte

---

## 🛑 Arrêter le mouvement

```mcfunction
# Stop any movement mode
/pvpbot stopmovement Bot1
```

Cette commande arrête :
- Mode suivi
- Mode escorte
- Passer au mode
- Suivi du chemin

---

## 👥 Mouvement des factions

Toutes les commandes de mouvement fonctionnent avec les factions :

```mcfunction
# Make entire faction follow a target
/pvpbot faction follow RedTeam Steve

# Make entire faction escort a target
/pvpbot faction escort RedTeam Steve

# Move entire faction to coordinates
/pvpbot faction goto RedTeam 100 64 200
```

---

## ⚙️ Paramètres de mouvement

| Paramètre | Tapez | Gamme | Par défaut | Descriptif |
|---------|------|-------|---------|-------------|
| `movespeed`| double | 0,1-2,0 | 1.0 | Vitesse de déplacement de base |
| `bhop`| booléen | - | vrai | Activer le lapin hop |
| `bhopcooldown`| entier | 5-30 | 12 | Tiques entre les sauts |
| `jumpboost`| double | 0,0-0,5 | 0,0 | Hauteur de saut supplémentaire |
| `gotousebaritone`| booléen | - | faux | Utilisez Baryton pour aller à |

---

## 🧭 Intégration Baryton

Activez Baritone pour une recherche de chemin avancée :

```mcfunction
/pvpbot settings gotousebaritone true
```

**Avantages:**
- Navigation sur terrain complexe
- Orientation longue distance
- Construction de ponts automatique
- Exploitation minière à travers les obstacles

**Exigences:**
- Le mod Baryton doit être installé
- Fonctionne uniquement avec les commandes goto
- Peut être plus lent que la recherche de chemin de base

---

## 🔧 Détails techniques

### Suivre la distance
- **Distance cible :** 3 blocs
- **Distance d'arrêt :** 2 blocs
- **Distance maximale :** 50 blocs (téléportation si dépassée)

### Fréquence de mise à jour
- Le mouvement est mis à jour à chaque tick (20 fois par seconde)
- Position cible vérifiée tous les 5 ticks
- Pathfinding recalculé en cas de besoin

### Gestion des obstacles
- Sauter automatiquement par-dessus des obstacles d'un bloc
- Orientation autour des murs et des barrières
- Nager dans l'eau
- Grimper aux échelles et aux vignes

---

## 🚨 Dépannage

### Le robot ne suit pas
- Vérifiez si la cible existe et est en ligne
- Vérifiez que le bot n'est pas bloqué ou bloqué
- Assurez-vous que le mouvement n'est pas désactivé
- Vérifiez si le bot est en combat (peut annuler le mouvement)

### Le robot reste bloqué
- Utiliser`/pvpbot stopmovement`et redémarrer
- Activer le baryton pour les terrains complexes
- Vérifiez les obstacles bloquant le chemin
- Téléporter le robot pour dégager la zone

### L'escorte ne défend pas
- Vérifiez que le mode escorte est actif (pas seulement suivre)
- Vérifiez si le tir ami est désactivé
- Assurez-vous que le bot dispose d'armes et de combat activés
- La cible doit réellement subir des dégâts pour déclencher la défense

---

## 💡 Conseils d'utilisation

### Suivi efficace
- Utiliser dans des zones ouvertes pour de meilleurs résultats
- Évitez les terrains encombrés ou complexes
- Gardez les cibles en mouvement à une vitesse raisonnable
- Utiliser une escorte pour les joueurs importants

### Navigation des coordonnées
- Utilisez goto pour un positionnement précis
- Activer le baryton pour les longues distances
- Vérifier que les coordonnées sont accessibles
- Utiliser des coordonnées relatives pour les mouvements à proximité

### Coordination des factions
- Organisez de grands groupes avec les commandes de faction
- Utiliser une escorte pour la protection VIP
- Coordonner les attaques avec la faction goto
- Arrivée étalée avec des commandes décalées