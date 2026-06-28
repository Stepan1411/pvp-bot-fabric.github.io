# Combat Strategies

Create powerful custom combat strategies for bots using the `CombatStrategy` interface. Strategies allow you to implement complex combat behaviors that integrate seamlessly with the bot's existing combat system.

## Overview

Combat strategies are executed in priority order during bot combat. Each strategy can:
- Check if it should be used in the current situation
- Execute custom combat logic
- Have cooldowns to prevent spam
- Override or supplement default combat behavior

## CombatStrategy Interface

```java
public interface CombatStrategy {
    String getName();                    // Unique strategy identifier
    int getPriority();                   // Execution priority (higher = first)
    boolean canUse(ServerPlayerEntity bot, Entity target, BotSettings settings);
    boolean execute(ServerPlayerEntity bot, Entity target, BotSettings settings, MinecraftServer server);
    default int getCooldown() { return 20; } // Cooldown in ticks (optional)
}
```

## Creating Strategies

### 1. Basic Potion Strategy

```java
package com.example.strategies;

import net.minecraft.entity.Entity;
import net.minecraft.entity.effect.StatusEffectInstance;
import net.minecraft.entity.effect.StatusEffects;
import net.minecraft.item.Items;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.network.ServerPlayerEntity;
import org.stepan1411.pvp_bot.api.combat.CombatStrategy;
import org.stepan1411.pvp_bot.bot.BotSettings;

public class StrengthPotionStrategy implements CombatStrategy {
    
    @Override
    public String getName() {
        return "StrengthPotion";
    }
    
    @Override
    public int getPriority() {
        return 120; // High priority - buffs before combat
    }
    
    @Override
    public boolean canUse(ServerPlayerEntity bot, Entity target, BotSettings settings) {
        // Only use if bot doesn't have strength and has potions
        return !bot.hasStatusEffect(StatusEffects.STRENGTH) &&
               bot.getInventory().contains(Items.POTION) &&
               bot.distanceTo(target) < 15.0; // Close enough to engage
    }
    
    @Override
    public boolean execute(ServerPlayerEntity bot, Entity target, BotSettings settings, MinecraftServer server) {
        // Apply strength effect
        bot.addStatusEffect(new StatusEffectInstance(
            StatusEffects.STRENGTH, 
            400, // 20 seconds
            1    // Level 2 (Strength II)
        ));
        
        // Optional: Send message
        bot.sendMessage(Text.literal("§cStrength activated!"));
        
        return true; // Strategy executed successfully
    }
    
    @Override
    public int getCooldown() {
        return 600; // 30 seconds cooldown
    }
}
```

### 2. Tactical Retreat Strategy

```java
public class TacticalRetreatStrategy implements CombatStrategy {
    
    @Override
    public String getName() {
        return "TacticalRetreat";
    }
    
    @Override
    public int getPriority() {
        return 200; // Highest priority - survival first
    }
    
    @Override
    public boolean canUse(ServerPlayerEntity bot, Entity target, BotSettings settings) {
        // Retreat when health is critically low
        return bot.getHealth() <= 4.0f && 
               bot.distanceTo(target) < 8.0; // Enemy is close
    }
    
    @Override
    public boolean execute(ServerPlayerEntity bot, Entity target, BotSettings settings, MinecraftServer server) {
        // Calculate retreat direction (opposite of target)
        Vec3d botPos = bot.getPos();
        Vec3d targetPos = target.getPos();
        Vec3d retreatDirection = botPos.subtract(targetPos).normalize();
        
        // Move away from target
        Vec3d retreatPos = botPos.add(retreatDirection.multiply(10));
        
        // Use ender pearl if available
        if (bot.getInventory().contains(Items.ENDER_PEARL)) {
            useEnderPearl(bot, retreatPos);
        } else {
            // Regular movement
            bot.teleport(retreatPos.x, retreatPos.y, retreatPos.z);
        }
        
        // Apply speed boost
        bot.addStatusEffect(new StatusEffectInstance(
            StatusEffects.SPEED, 
            100, // 5 seconds
            2    // Speed III
        ));
        
        bot.sendMessage(Text.literal("§eRetreating!"));
        return true;
    }
    
    private void useEnderPearl(ServerPlayerEntity bot, Vec3d targetPos) {
        // Find and use ender pearl
        for (int i = 0; i < bot.getInventory().size(); i++) {
            ItemStack stack = bot.getInventory().getStack(i);
            if (stack.getItem() == Items.ENDER_PEARL) {
                bot.setStackInHand(Hand.MAIN_HAND, stack);
                // Throw ender pearl toward retreat position
                bot.interactItem(Hand.MAIN_HAND);
                break;
            }
        }
    }
    
    @Override
    public int getCooldown() {
        return 200; // 10 seconds
    }
}
```

### 3. Environmental Adaptation Strategy

```java
public class EnvironmentalStrategy implements CombatStrategy {
    
    @Override
    public String getName() {
        return "EnvironmentalAdaptation";
    }
    
    @Override
    public int getPriority() {
        return 90;
    }
    
    @Override
    public boolean canUse(ServerPlayerEntity bot, Entity target, BotSettings settings) {
        World world = bot.getWorld();
        
        // Different conditions for different environments
        if (world.getRegistryKey() == World.NETHER) {
            return !bot.hasStatusEffect(StatusEffects.FIRE_RESISTANCE);
        } else if (world.getRegistryKey() == World.END) {
            return !bot.hasStatusEffect(StatusEffects.SLOW_FALLING);
        } else if (bot.isSubmergedInWater()) {
            return !bot.hasStatusEffect(StatusEffects.WATER_BREATHING);
        }
        
        return false;
    }
    
    @Override
    public boolean execute(ServerPlayerEntity bot, Entity target, BotSettings settings, MinecraftServer server) {
        World world = bot.getWorld();
        
        if (world.getRegistryKey() == World.NETHER) {
            // Fire resistance in Nether
            bot.addStatusEffect(new StatusEffectInstance(
                StatusEffects.FIRE_RESISTANCE, 6000, 0));
            bot.sendMessage(Text.literal("§6Fire resistance activated!"));
            
        } else if (world.getRegistryKey() == World.END) {
            // Slow falling in End
            bot.addStatusEffect(new StatusEffectInstance(
                StatusEffects.SLOW_FALLING, 1200, 0));
            bot.sendMessage(Text.literal("§dSlow falling activated!"));
            
        } else if (bot.isSubmergedInWater()) {
            // Water breathing underwater
            bot.addStatusEffect(new StatusEffectInstance(
                StatusEffects.WATER_BREATHING, 1200, 0));
            bot.sendMessage(Text.literal("§bWater breathing activated!"));
        }
        
        return true;
    }
    
    @Override
    public int getCooldown() {
        return 100; // 5 seconds
    }
}
```

### 4. Team Coordination Strategy

```java
public class TeamCoordinationStrategy implements CombatStrategy {
    
    @Override
    public String getName() {
        return "TeamCoordination";
    }
    
    @Override
    public int getPriority() {
        return 110;
    }
    
    @Override
    public boolean canUse(ServerPlayerEntity bot, Entity target, BotSettings settings) {
        // Check if there are allied bots nearby
        List<ServerPlayerEntity> allies = getNearbyAllies(bot, 15.0);
        return allies.size() >= 2; // At least 2 allies nearby
    }
    
    @Override
    public boolean execute(ServerPlayerEntity bot, Entity target, BotSettings settings, MinecraftServer server) {
        List<ServerPlayerEntity> allies = getNearbyAllies(bot, 15.0);
        
        // Coordinate attack patterns
        if (allies.size() >= 3) {
            // Surround target
            surroundTarget(bot, allies, target);
        } else {
            // Pincer attack
            pincerAttack(bot, allies, target);
        }
        
        // Apply team buffs
        for (ServerPlayerEntity ally : allies) {
            ally.addStatusEffect(new StatusEffectInstance(
                StatusEffects.STRENGTH, 200, 0));
        }
        
        return true;
    }
    
    private List<ServerPlayerEntity> getNearbyAllies(ServerPlayerEntity bot, double radius) {
        return bot.getWorld().getPlayers().stream()
            .filter(p -> PvpBotAPI.isBot(p.getName().getString()))
            .filter(p -> !p.equals(bot))
            .filter(p -> p.distanceTo(bot) <= radius)
            .collect(Collectors.toList());
    }
    
    private void surroundTarget(ServerPlayerEntity bot, List<ServerPlayerEntity> allies, Entity target) {
        Vec3d targetPos = target.getPos();
        double angleStep = 2 * Math.PI / (allies.size() + 1);
        
        // Position bots in circle around target
        for (int i = 0; i < allies.size(); i++) {
            double angle = i * angleStep;
            Vec3d pos = targetPos.add(
                Math.cos(angle) * 5, 0, Math.sin(angle) * 5);
            allies.get(i).teleport(pos.x, pos.y, pos.z);
        }
    }
    
    private void pincerAttack(ServerPlayerEntity bot, List<ServerPlayerEntity> allies, Entity target) {
        // Position allies on opposite sides of target
        Vec3d targetPos = target.getPos();
        Vec3d botPos = bot.getPos();
        Vec3d direction = targetPos.subtract(botPos).normalize();
        
        if (!allies.isEmpty()) {
            Vec3d flankerPos = targetPos.add(direction.multiply(-5));
            allies.get(0).teleport(flankerPos.x, flankerPos.y, flankerPos.z);
        }
    }
    
    @Override
    public int getCooldown() {
        return 300; // 15 seconds
    }
}
```

### 5. Weapon-Specific Strategy

```java
public class MaceSpecialStrategy implements CombatStrategy {
    
    @Override
    public String getName() {
        return "MaceSpecial";
    }
    
    @Override
    public int getPriority() {
        return 80;
    }
    
    @Override
    public boolean canUse(ServerPlayerEntity bot, Entity target, BotSettings settings) {
        // Only use with mace equipped
        ItemStack mainHand = bot.getMainHandStack();
        return mainHand.getItem() == Items.MACE &&
               settings.isMaceEnabled() &&
               bot.distanceTo(target) <= settings.getMaceRange();
    }
    
    @Override
    public boolean execute(ServerPlayerEntity bot, Entity target, BotSettings settings, MinecraftServer server) {
        // Jump for increased mace damage
        if (bot.isOnGround()) {
            bot.jump();
            
            // Schedule attack for when bot is falling
            server.execute(() -> {
                if (bot.getVelocity().y < 0) { // Falling
                    bot.attack(target);
                    
                    // Add knockback effect
                    if (target instanceof LivingEntity living) {
                        Vec3d knockback = bot.getPos().subtract(target.getPos())
                            .normalize().multiply(-2.0);
                        living.addVelocity(knockback.x, 0.5, knockback.z);
                    }
                }
            });
        }
        
        return true;
    }
    
    @Override
    public int getCooldown() {
        return 60; // 3 seconds
    }
}
```

## Strategy Registration

Register your strategies in your mod's `onInitialize` method:

```java
import org.stepan1411.pvp_bot.api.combat.CombatStrategyRegistry;

public class MyBotAddon implements ModInitializer {
    @Override
    public void onInitialize() {
        CombatStrategyRegistry registry = CombatStrategyRegistry.getInstance();
        
        // Register all strategies
        registry.register(new StrengthPotionStrategy());
        registry.register(new TacticalRetreatStrategy());
        registry.register(new EnvironmentalStrategy());
        registry.register(new TeamCoordinationStrategy());
        registry.register(new MaceSpecialStrategy());
        
        System.out.println("Registered " + registry.getStrategies().size() + " combat strategies");
    }
}
```

## Priority System

Strategies are executed in priority order (highest first):

| Priority Range | Purpose | Examples |
|----------------|---------|----------|
| **200+** | Critical survival | Retreat, emergency healing |
| **150-199** | High-priority combat | Crystal PvP, anchor PvP |
| **100-149** | Combat preparation | Buffs, debuffs, positioning |
| **50-99** | Special attacks | Weapon abilities, environmental |
| **1-49** | Basic combat | Default melee, ranged attacks |

### Built-in Strategy Priorities

The mod includes these built-in strategies:
- **ElytraMace** - 160
- **Crystal PvP** - 150  
- **Anchor PvP** - 140
- **Mace Combat** - 100
- **Ranged Combat** - 50
- **Melee Combat** - 10

## Advanced Features

### 1. Strategy Chaining

```java
public class ChainedStrategy implements CombatStrategy {
    private final List<CombatStrategy> subStrategies;
    
    public ChainedStrategy() {
        subStrategies = Arrays.asList(
            new BuffStrategy(),
            new PositionStrategy(),
            new AttackStrategy()
        );
    }
    
    @Override
    public boolean execute(ServerPlayerEntity bot, Entity target, BotSettings settings, MinecraftServer server) {
        for (CombatStrategy strategy : subStrategies) {
            if (strategy.canUse(bot, target, settings)) {
                if (strategy.execute(bot, target, settings, server)) {
                    return true; // First successful strategy wins
                }
            }
        }
        return false;
    }
}
```

### 2. Conditional Strategy

```java
public class ConditionalStrategy implements CombatStrategy {
    
    @Override
    public boolean canUse(ServerPlayerEntity bot, Entity target, BotSettings settings) {
        // Complex conditions
        boolean healthOk = bot.getHealth() > 10.0f;
        boolean hasResources = checkResources(bot);
        boolean rightTime = bot.getWorld().getTimeOfDay() % 24000 > 12000; // Night
        boolean rightWeather = bot.getWorld().isRaining();
        
        return healthOk && hasResources && rightTime && rightWeather;
    }
    
    private boolean checkResources(ServerPlayerEntity bot) {
        return bot.getInventory().contains(Items.DIAMOND_SWORD) &&
               bot.getInventory().contains(Items.GOLDEN_APPLE);
    }
}
```

### 3. Adaptive Strategy

```java
public class AdaptiveStrategy implements CombatStrategy {
    private final Map<String, Integer> targetCounters = new HashMap<>();
    
    @Override
    public boolean execute(ServerPlayerEntity bot, Entity target, BotSettings settings, MinecraftServer server) {
        String targetType = target.getClass().getSimpleName();
        int encounters = targetCounters.getOrDefault(targetType, 0);
        
        // Adapt strategy based on previous encounters
        if (encounters < 3) {
            // Aggressive approach for new targets
            return aggressiveAttack(bot, target);
        } else {
            // Cautious approach for familiar targets
            return cautiousAttack(bot, target);
        }
    }
    
    private boolean aggressiveAttack(ServerPlayerEntity bot, Entity target) {
        // Direct attack
        bot.attack(target);
        return true;
    }
    
    private boolean cautiousAttack(ServerPlayerEntity bot, Entity target) {
        // Defensive approach
        if (bot.distanceTo(target) > 5.0) {
            // Keep distance and use ranged
            return useRangedAttack(bot, target);
        }
        return false;
    }
}
```

## Debugging and Testing

### 1. Debug Logging

```java
@Override
public boolean execute(ServerPlayerEntity bot, Entity target, BotSettings settings, MinecraftServer server) {
    String botName = bot.getName().getString();
    String targetName = target.getName().getString();
    
    System.out.println("[" + getName() + "] Executing for " + botName + " vs " + targetName);
    System.out.println("[" + getName() + "] Bot health: " + bot.getHealth());
    System.out.println("[" + getName() + "] Distance: " + bot.distanceTo(target));
    
    try {
        // Your strategy logic
        boolean result = executeStrategy(bot, target, settings, server);
        
        System.out.println("[" + getName() + "] Result: " + result);
        return result;
        
    } catch (Exception e) {
        System.err.println("[" + getName() + "] Error: " + e.getMessage());
        return false;
    }
}
```

### 2. Strategy Testing

```java
public class StrategyTester {
    public static void testStrategy(CombatStrategy strategy, ServerPlayerEntity bot, Entity target) {
        BotSettings settings = PvpBotAPI.getBotSettings();
        MinecraftServer server = bot.getServer();
        
        System.out.println("Testing strategy: " + strategy.getName());
        System.out.println("Priority: " + strategy.getPriority());
        System.out.println("Can use: " + strategy.canUse(bot, target, settings));
        
        if (strategy.canUse(bot, target, settings)) {
            boolean result = strategy.execute(bot, target, settings, server);
            System.out.println("Execution result: " + result);
            System.out.println("Cooldown: " + strategy.getCooldown() + " ticks");
        }
    }
}
```

## Best Practices

### 1. Performance Optimization

```java
@Override
public boolean canUse(ServerPlayerEntity bot, Entity target, BotSettings settings) {
    // Fast checks first
    if (bot.getHealth() > 15.0f) return false;
    if (bot.distanceTo(target) > 20.0) return false;
    
    // Expensive checks last
    return hasRequiredItems(bot) && checkComplexConditions(bot, target);
}
```

### 2. Error Handling

```java
@Override
public boolean execute(ServerPlayerEntity bot, Entity target, BotSettings settings, MinecraftServer server) {
    try {
        return executeInternal(bot, target, settings, server);
    } catch (Exception e) {
        System.err.println("Strategy " + getName() + " failed: " + e.getMessage());
        return false; // Fail gracefully
    }
}
```

### 3. Resource Management

```java
private boolean consumeResource(ServerPlayerEntity bot, Item item) {
    for (int i = 0; i < bot.getInventory().size(); i++) {
        ItemStack stack = bot.getInventory().getStack(i);
        if (stack.getItem() == item) {
            stack.decrement(1);
            return true;
        }
    }
    return false;
}
```

### 4. Cooldown Management

```java
public class CooldownManager {
    private final Map<String, Long> lastUsed = new HashMap<>();
    
    public boolean canUseStrategy(String strategyName, int cooldownTicks) {
        long currentTime = System.currentTimeMillis();
        long lastUseTime = lastUsed.getOrDefault(strategyName, 0L);
        long cooldownMs = cooldownTicks * 50; // Convert ticks to ms
        
        return currentTime - lastUseTime >= cooldownMs;
    }
    
    public void markUsed(String strategyName) {
        lastUsed.put(strategyName, System.currentTimeMillis());
    }
}
```

## Integration with Events

Combine strategies with events for comprehensive bot control:

```java
public class IntegratedCombatSystem implements ModInitializer {
    @Override
    public void onInitialize() {
        // Register strategy
        CombatStrategyRegistry.getInstance().register(new MyStrategy());
        
        // Register events
        PvpBotAPI.getEventManager().registerAttackHandler((bot, target) -> {
            // Pre-attack logic
            return false; // Allow attack
        });
    }
}
```

Combat strategies provide powerful customization for bot behavior. Experiment with different approaches and combine multiple strategies for complex combat systems!
