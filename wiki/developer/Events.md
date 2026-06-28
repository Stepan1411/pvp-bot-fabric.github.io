# Events

PVP Bot API provides a comprehensive event system for tracking bot lifecycle and behavior.

## Event Manager

All event handlers are registered through the singleton `BotEventManager`:

```java
BotEventManager eventManager = PvpBotAPI.getEventManager();
```

## Event Types

### 1. BotSpawnHandler

**Trigger:** When a bot spawns in the world  
**Cancellable:** No  
**Frequency:** Once per bot spawn

```java
eventManager.registerSpawnHandler(bot -> {
    System.out.println("Bot spawned: " + bot.getName().getString());
    
    // Initialize bot state
    bot.setHealth(20.0f);
    
    // Give starting equipment
    ItemStack sword = new ItemStack(Items.IRON_SWORD);
    bot.getInventory().setStack(0, sword);
    
    // Set custom data
    bot.getDataTracker().set(/* custom data */);
});
```

**Use Cases:**
- Initialize bot equipment
- Set custom bot properties
- Log spawn events
- Send welcome messages

### 2. BotDeathHandler

**Trigger:** When a bot dies or is removed  
**Cancellable:** No  
**Frequency:** Once per bot death

```java
eventManager.registerDeathHandler(bot -> {
    String botName = bot.getName().getString();
    System.out.println("Bot died: " + botName);
    
    // Save death statistics
    saveDeathStats(botName, bot.getPos());
    
    // Drop custom items
    dropCustomLoot(bot);
    
    // Schedule respawn
    scheduleRespawn(botName, 100); // 5 seconds
});
```

**Use Cases:**
- Death statistics tracking
- Custom loot drops
- Respawn scheduling
- Achievement systems

### 3. BotAttackHandler

**Trigger:** When a bot is about to attack an entity  
**Cancellable:** Yes  
**Frequency:** Every attack attempt

```java
eventManager.registerAttackHandler((bot, target) -> {
    String botName = bot.getName().getString();
    String targetName = target.getName().getString();
    
    System.out.println(botName + " attacks " + targetName);
    
    // Cancel attack on villagers
    if (target instanceof VillagerEntity) {
        System.out.println("Protecting villager from " + botName);
        return true; // Cancel attack
    }
    
    // Cancel attack on faction members
    if (target instanceof PlayerEntity player) {
        if (isSameFaction(botName, player.getName().getString())) {
            return true; // Cancel friendly fire
        }
    }
    
    // Apply custom damage modifiers
    if (target instanceof PlayerEntity) {
        applyPvpModifiers(bot, target);
    }
    
    return false; // Allow attack
});
```

**Return Values:**
- `true` - Cancel the attack
- `false` - Allow the attack

**Use Cases:**
- Faction protection
- Entity-specific rules
- Custom damage calculations
- Attack logging

### 4. BotDamageHandler

**Trigger:** When a bot is about to take damage  
**Cancellable:** Yes  
**Frequency:** Every damage event

```java
eventManager.registerDamageHandler((bot, attacker, damage) -> {
    String botName = bot.getName().getString();
    System.out.println(botName + " taking " + damage + " damage");
    
    // Make bot immune to fall damage
    if (attacker == null) { // Environmental damage
        DamageSource lastDamage = bot.getRecentDamageSource();
        if (lastDamage != null && lastDamage.isOf(DamageTypes.FALL)) {
            return true; // Cancel fall damage
        }
    }
    
    // Reduce damage from specific sources
    if (attacker instanceof CreeperEntity) {
        // Apply custom damage reduction
        float reducedDamage = damage * 0.5f;
        bot.damage(DamageSource.explosion(attacker), reducedDamage);
        return true; // Cancel original damage
    }
    
    // God mode for low health
    if (bot.getHealth() <= 2.0f) {
        System.out.println("God mode activated for " + botName);
        return true; // Cancel damage
    }
    
    return false; // Allow damage
});
```

**Parameters:**
- `bot` - The bot taking damage
- `attacker` - Entity causing damage (can be null for environmental)
- `damage` - Amount of damage

**Return Values:**
- `true` - Cancel the damage
- `false` - Allow the damage

**Use Cases:**
- Damage immunity systems
- Custom damage calculations
- Protection mechanics
- Health-based rules

### 5. BotTickHandler

**Trigger:** Every game tick (20 times per second)  
**Cancellable:** No  
**Frequency:** 20 times per second per bot

```java
eventManager.registerTickHandler(bot -> {
    String botName = bot.getName().getString();
    
    // Regeneration every 5 seconds (100 ticks)
    if (bot.age % 100 == 0) {
        if (bot.getHealth() < bot.getMaxHealth()) {
            bot.setHealth(Math.min(bot.getMaxHealth(), bot.getHealth() + 1.0f));
        }
    }
    
    // Check for special conditions
    if (bot.age % 20 == 0) { // Every second
        checkSpecialConditions(bot);
    }
    
    // Update custom AI
    updateCustomBehavior(bot);
});
```

**⚠️ Performance Warning:** This handler is called very frequently (20 times per second per bot). Avoid heavy operations!

**Use Cases:**
- Custom regeneration
- Periodic checks
- Custom AI behaviors
- Status updates

## Advanced Examples

### 1. Bot Statistics System

```java
public class BotStatsTracker {
    private final Map<String, BotStats> stats = new HashMap<>();
    
    public void register() {
        BotEventManager manager = PvpBotAPI.getEventManager();
        
        // Track spawns
        manager.registerSpawnHandler(bot -> {
            String name = bot.getName().getString();
            stats.computeIfAbsent(name, k -> new BotStats()).spawns++;
        });
        
        // Track deaths
        manager.registerDeathHandler(bot -> {
            String name = bot.getName().getString();
            stats.computeIfAbsent(name, k -> new BotStats()).deaths++;
        });
        
        // Track attacks
        manager.registerAttackHandler((bot, target) -> {
            String name = bot.getName().getString();
            stats.computeIfAbsent(name, k -> new BotStats()).attacks++;
            return false; // Don't cancel
        });
        
        // Track damage taken
        manager.registerDamageHandler((bot, attacker, damage) -> {
            String name = bot.getName().getString();
            BotStats botStats = stats.computeIfAbsent(name, k -> new BotStats());
            botStats.damageTaken += damage;
            return false; // Don't cancel
        });
    }
    
    public BotStats getStats(String botName) {
        return stats.getOrDefault(botName, new BotStats());
    }
    
    public static class BotStats {
        public int spawns = 0;
        public int deaths = 0;
        public int attacks = 0;
        public float damageTaken = 0.0f;
        
        public double getKDRatio() {
            return deaths == 0 ? attacks : (double) attacks / deaths;
        }
    }
}
```

### 2. Faction System Integration

```java
public class FactionEventHandler {
    private final Map<String, String> botFactions = new HashMap<>();
    
    public void register() {
        BotEventManager manager = PvpBotAPI.getEventManager();
        
        // Prevent friendly fire
        manager.registerAttackHandler((bot, target) -> {
            if (target instanceof PlayerEntity player) {
                String botFaction = getBotFaction(bot.getName().getString());
                String targetFaction = getBotFaction(player.getName().getString());
                
                if (botFaction != null && botFaction.equals(targetFaction)) {
                    // Same faction - cancel attack
                    bot.sendMessage(Text.literal("Cannot attack faction member!"));
                    return true;
                }
            }
            return false;
        });
        
        // Faction-based damage reduction
        manager.registerDamageHandler((bot, attacker, damage) -> {
            if (attacker instanceof PlayerEntity player) {
                String botFaction = getBotFaction(bot.getName().getString());
                String attackerFaction = getBotFaction(player.getName().getString());
                
                if (botFaction != null && botFaction.equals(attackerFaction)) {
                    // Reduce friendly fire damage by 50%
                    float reducedDamage = damage * 0.5f;
                    bot.damage(bot.getRecentDamageSource(), reducedDamage);
                    return true; // Cancel original damage
                }
            }
            return false;
        });
    }
    
    private String getBotFaction(String botName) {
        return botFactions.get(botName);
    }
    
    public void setBotFaction(String botName, String faction) {
        botFactions.put(botName, faction);
    }
}
```

### 3. Auto-Respawn System

```java
public class AutoRespawnSystem {
    private final Map<String, Integer> respawnDelays = new HashMap<>();
    
    public void register() {
        PvpBotAPI.getEventManager().registerDeathHandler(bot -> {
            String botName = bot.getName().getString();
            MinecraftServer server = bot.getServer();
            
            // Get respawn delay (default 5 seconds)
            int delay = respawnDelays.getOrDefault(botName, 100);
            
            // Schedule respawn
            scheduleRespawn(server, botName, delay);
            
            // Announce death
            server.getPlayerManager().broadcast(
                Text.literal("§c" + botName + " died! Respawning in " + (delay/20) + " seconds..."),
                false
            );
        });
    }
    
    private void scheduleRespawn(MinecraftServer server, String botName, int delay) {
        if (delay <= 0) {
            // Respawn the bot
            server.getCommandManager().getDispatcher().execute(
                "pvpbot spawn " + botName,
                server.getCommandSource()
            );
        } else {
            // Wait one more tick
            server.execute(() -> scheduleRespawn(server, botName, delay - 1));
        }
    }
    
    public void setRespawnDelay(String botName, int ticks) {
        respawnDelays.put(botName, ticks);
    }
}
```

### 4. Custom Bot Behavior

```java
public class CustomBotBehavior {
    private final Map<String, BotState> botStates = new HashMap<>();
    
    public void register() {
        BotEventManager manager = PvpBotAPI.getEventManager();
        
        // Initialize bot state on spawn
        manager.registerSpawnHandler(bot -> {
            String name = bot.getName().getString();
            botStates.put(name, new BotState());
        });
        
        // Update behavior every tick
        manager.registerTickHandler(bot -> {
            String name = bot.getName().getString();
            BotState state = botStates.get(name);
            if (state == null) return;
            
            // Custom behavior based on health
            if (bot.getHealth() < 6.0f && !state.isRetreating) {
                startRetreat(bot, state);
            } else if (bot.getHealth() > 15.0f && state.isRetreating) {
                stopRetreat(bot, state);
            }
            
            // Update state
            state.ticksAlive++;
        });
        
        // Clean up on death
        manager.registerDeathHandler(bot -> {
            botStates.remove(bot.getName().getString());
        });
    }
    
    private void startRetreat(ServerPlayerEntity bot, BotState state) {
        state.isRetreating = true;
        // Implement retreat logic
        bot.sendMessage(Text.literal("§eRetreating!"));
    }
    
    private void stopRetreat(ServerPlayerEntity bot, BotState state) {
        state.isRetreating = false;
        bot.sendMessage(Text.literal("§aRe-engaging!"));
    }
    
    private static class BotState {
        boolean isRetreating = false;
        int ticksAlive = 0;
    }
}
```

## Event Execution

### Order
Events are executed in the order handlers were registered. Multiple handlers for the same event will all be called.

### Cancellation
For cancellable events (Attack, Damage), if any handler returns `true`, the event is cancelled. However, all handlers are still called.

### Error Handling
All exceptions in event handlers are caught and logged. An error in one handler won't prevent other handlers from executing.

```java
// Example of safe event handling
manager.registerAttackHandler((bot, target) -> {
    try {
        // Your logic here
        return customAttackLogic(bot, target);
    } catch (Exception e) {
        System.err.println("Error in attack handler: " + e.getMessage());
        return false; // Default behavior on error
    }
});
```

### Performance Considerations

1. **Tick Handlers:** Keep tick handler logic minimal - it runs 20 times per second per bot
2. **Heavy Operations:** Use async processing for database operations or file I/O
3. **Caching:** Cache frequently accessed data instead of recalculating
4. **Conditional Logic:** Use early returns to avoid unnecessary processing

```java
// Good: Early return for performance
manager.registerTickHandler(bot -> {
    // Only process every 20 ticks (1 second)
    if (bot.age % 20 != 0) return;
    
    // Your logic here
});

// Bad: Heavy operation every tick
manager.registerTickHandler(bot -> {
    // This runs 20 times per second!
    expensiveCalculation(bot);
});
```

## Integration with Combat Strategies

Events can be used alongside combat strategies for comprehensive bot control:

```java
public class IntegratedBotSystem {
    public void register() {
        // Register events
        PvpBotAPI.getEventManager().registerAttackHandler(this::handleAttack);
        
        // Register combat strategy
        CombatStrategyRegistry.getInstance().register(new CustomStrategy());
    }
    
    private boolean handleAttack(ServerPlayerEntity bot, Entity target) {
        // Event-based attack filtering
        if (shouldCancelAttack(bot, target)) {
            return true;
        }
        return false;
    }
    
    private class CustomStrategy implements CombatStrategy {
        // Strategy-based combat logic
        // ...
    }
}
```
