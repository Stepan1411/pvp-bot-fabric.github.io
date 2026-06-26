# 🚶 Movement System

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

**Behavior:**
- Maintains 3-block distance from target
- Automatically avoids obstacles
- Follows across dimensions
- Uses smart pathfinding
- Stops when target is offline

### Escort Mode
Enhanced follow mode with defensive capabilities.

```mcfunction
# Make bot escort a player
/pvpbot escort Bot1 Steve

# Make bot escort another bot
/pvpbot escort Bot1 Bot2
```

**Behavior:**
- Same as follow mode
- **Automatically defends target** if attacked
- Prioritizes target protection over other combat
- Attacks anyone who damages the escorted target

### Goto Mode
Direct coordinate-based movement.

```mcfunction
# Send bot to coordinates
/pvpbot goto Bot1 100 64 200

# Use relative coordinates
/pvpbot goto Bot1 ~10 ~ ~-5
```

**Behavior:**
- Smart pathfinding to coordinates
- Obstacle avoidance and jumping
- Optional Baritone integration
- Stops when destination is reached

---

## 🛑 Stopping Movement

```mcfunction
# Stop any movement mode
/pvpbot stopmovement Bot1
```

This command stops:
- Follow mode
- Escort mode  
- Goto mode
- Path following

---

## 👥 Faction Movement

All movement commands work with factions:

```mcfunction
# Make entire faction follow a target
/pvpbot faction follow RedTeam Steve

# Make entire faction escort a target
/pvpbot faction escort RedTeam Steve

# Move entire faction to coordinates
/pvpbot faction goto RedTeam 100 64 200
```

---

## ⚙️ Movement Settings

| Setting | Type | Range | Default | Description |
|---------|------|-------|---------|-------------|
| `movespeed` | double | 0.1-2.0 | 1.0 | Base movement speed |
| `bhop` | bool | - | true | Enable bunny hop |
| `bhopcooldown` | int | 5-30 | 12 | Ticks between jumps |
| `jumpboost` | double | 0.0-0.5 | 0.0 | Extra jump height |
| `gotousebaritone` | bool | - | false | Use Baritone for goto |

---

## 🧭 Baritone Integration

Enable Baritone for advanced pathfinding:

```mcfunction
/pvpbot settings gotousebaritone true
```

**Benefits:**
- Complex terrain navigation
- Long-distance pathfinding
- Automatic bridge building
- Mining through obstacles

**Requirements:**
- Baritone mod must be installed
- Only works with goto commands
- May be slower than basic pathfinding

---

## 🔧 Technical Details

### Follow Distance
- **Target distance:** 3 blocks
- **Stop distance:** 2 blocks  
- **Max distance:** 50 blocks (teleport if exceeded)

### Update Frequency
- Movement updates every tick (20 times per second)
- Target position checked every 5 ticks
- Pathfinding recalculated when needed

### Obstacle Handling
- Automatic jumping over 1-block obstacles
- Pathfinding around walls and barriers
- Swimming through water
- Climbing ladders and vines

---

## 🚨 Troubleshooting

### Bot doesn't follow
- Check if target exists and is online
- Verify bot isn't stuck or blocked
- Ensure movement isn't disabled
- Check if bot is in combat (may override movement)

### Bot gets stuck
- Use `/pvpbot stopmovement` and restart
- Enable Baritone for complex terrain
- Check for obstacles blocking the path
- Teleport bot to clear area

### Escort not defending
- Verify escort mode is active (not just follow)
- Check if friendly fire is disabled
- Ensure bot has weapons and combat enabled
- Target must actually take damage to trigger defense

---

## 💡 Usage Tips

### Effective Following
- Use in open areas for best results
- Avoid crowded or complex terrain
- Keep targets moving at reasonable speed
- Use escort for important players

### Coordinate Navigation
- Use goto for precise positioning
- Enable Baritone for long distances
- Check coordinates are accessible
- Use relative coordinates for nearby movement

### Faction Coordination
- Organize large groups with faction commands
- Use escort for VIP protection
- Coordinate attacks with faction goto
- Spread out arrival with staggered commands