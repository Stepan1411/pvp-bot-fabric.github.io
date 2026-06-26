# Explosive Combat

Bots can use Crystal PVP and Respawn Anchor PVP when equipped with the right items.

## Crystal PVP

Requires: **Obsidian** + **End Crystals**

### Activation
- Auto-selected when target is 2.5-8 blocks away
- Enabled by default (`crystalpvp` setting)

### Combat Flow
1. **Step 0 - Place Obsidian**: Finds a position next to the target, places obsidian
2. **Step 1 - Place Crystal**: Puts end crystal on the obsidian
3. **Step 2 - Attack Crystal**: Hits the crystal to detonate it near the target
4. **Repeat**: Moves back to Step 1 or 0 depending on distance

### Features
- Reuses existing obsidian blocks near targets
- Sword attacks between steps for extra damage
- Stuck detection: resets after 100 ticks on same step
- Retries failed placements up to 3 times
- Maintains optimal distance (3.0-5.5 blocks)
- Tracks failed positions to avoid retrying

### Commands
```
/pvpbot settings crystalpvp true
```

## Anchor PVP

Requires: **Respawn Anchor** + **Glowstone**

**Note:** Does not work in the Nether dimension.

### Activation
- Auto-selected when target is 2.0-8.0 blocks away
- Requires health above 40% (self-damage protection)
- Enabled by default (`anchorpvp` setting)

### Combat Flow
1. **Step 0 - Place Anchor**: Finds position next to target, places respawn anchor
2. **Step 1 - Charge Anchor**: Uses glowstone to charge the anchor
3. **Step 2 - Detonate**: Right-clicks the charged anchor to explode

### Features
- Reuses existing anchors near targets
- Stuck detection with auto-reset
- Retreats if too close to anchor before detonation

### Commands
```
/pvpbot settings anchorpvp true
```

## Settings

| Setting | Default | Description |
|---------|---------|-------------|
| crystalpvp | true | Enable Crystal PVP combat |
| anchorpvp | true | Enable Anchor PVP combat |
