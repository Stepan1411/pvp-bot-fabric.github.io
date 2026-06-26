# ElytraMace Combat

The ElytraMace technique is an advanced aerial combat maneuver where the bot:
1. Equips elytra and launches upward with fireworks
2. Removes elytra mid-air
3. Slams down with a mace for massive fall-damage bonus

## Requirements

- **Elytra** (in inventory)
- **Firework Rockets** (in inventory)
- **Mace** (in inventory)
- Settings: `mace` and `elytramace` enabled

## Activation

ElytraMace activates automatically when:
- Bot has all required items
- Bot has a target (from revenge or forced attack)
- Bot is on the ground

## Combat Phases

1. **Phase 0-1**: Equip elytra, move firework to hotbar
2. **Phase 2-3**: Jump and ascend
3. **Phase 4-5**: Deploy firework rocket, gain altitude
4. **Phase 6**: Wait for ascent
5. **Phase 7**: Remove elytra, equip chestplate (if available)
6. **Phase 8-9**: Restore elytra for next cycle
7. **Phase 10-11**: Jump, equip mace, slam target

Total cycle timeout: 300 ticks (15 seconds)

## Wind Burst Variant

If the mace has the **Wind Burst** enchantment, the bot uses a modified sequence:
1. Equip elytra, fly upward
2. Launch with fireworks
3. Remove elytra mid-air
4. Mace-slam the target
5. Wind Burst launches bot upward again for follow-up attacks

## Commands

```
/pvpbot settings mace true
/pvpbot settings elytramace true
```
