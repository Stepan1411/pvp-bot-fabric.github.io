# Pathfinding

Bot navigation and pathfinding systems in PVP Bot API.

## Overview

PVP Bot uses multiple pathfinding systems:
- **Baritone Integration** - Advanced pathfinding for complex navigation
- **Built-in Navigation** - Simple point-to-point movement
- **Custom Pathfinding** - API for implementing custom navigation

## Baritone Integration

The mod integrates with Baritone for advanced pathfinding capabilities.

### Baritone Settings

```java
BotSettings settings = PvpBotAPI.getBotSettings();

// Global Baritone usage
boolean useBaritone = settings.isUseBaritone();

// Command-specific Baritone usage
boolean gotoUseBaritone = settings.isGotoUseBaritone();
boolean escortUseBaritone = settings.isEscortUseBaritone();
boolean followUseBaritone = settings.isFollowUseBaritone();
```

### Accessing Baritone State

```java
// Check if bot is using Baritone pathfinding
ServerPlayerEntity bot = PvpBotAPI.getBot(server, "BotName");
if (bot != null) {
    // Baritone state is managed internally
    // Use events to react to pathfinding changes
}
```

## Built-in Navigation

### Movement Commands

Bots support several movement commands:

```java
// Teleport bot to coordinates
/pvpbot goto BotName 100 64 200

// Make bot follow a player
/pvpbot follow BotName PlayerName

// Make bot escort a player (follow at distance)
/pvpbot escort BotName PlayerName

// Stop bot movement
/pvpbot stop BotName
```

### Movement Settings

```java
BotSettings settings = PvpBotAPI.getBotSettings();

// Movement speed multiplier
double moveSpeed = settings.getMoveSpeed(); // 0.1 - 2.0

// Bunny hopping
boolean bhopEnabled = settings.isBhopEnabled();
int bhopCooldown = settings.getBhopCooldown(); // ticks

// Jump boost
double jumpBoost = settings.getJumpBoost(); // 0.0 - 0.5

// Idle wandering
boolean idleWander = settings.isIdleWanderEnabled();
double wanderRadius = settings.getIdleWanderRadius(); // blocks
```

## Custom Pathfinding

### Creating Custom Navigation

You can implement custom pathfinding using events and combat strategies:

```java
public class CustomPathfinding implements ModInitializer {
    
    private final Map<String, NavigationGoal> botGoals = new HashMap<>();
    
    @Override
    public void onInitialize() {
        // Update bot positions every tick
        PvpBotAPI.getEventManager().registerTickHandler(bot -> {
            String botName = bot.getName().getString();
            NavigationGoal goal = botGoals.get(botName);
            
            if (goal != null && !goal.isReached(bot)) {
                moveTowardsGoal(bot, goal);
            }
        });
    }
    
    public void setGoal(String botName, Vec3d target) {
        botGoals.put(botName, new NavigationGoal(target));
    }
    
    private void moveTowardsGoal(ServerPlayerEntity bot, NavigationGoal goal) {
        Vec3d botPos = bot.getPos();
        Vec3d direction = goal.target.subtract(botPos).normalize();
        
        // Simple movement - can be enhanced with pathfinding algorithms
        Vec3d newPos = botPos.add(direction.multiply(0.5));
        bot.teleport(newPos.x, newPos.y, newPos.z);
    }
    
    private static class NavigationGoal {
        final Vec3d target;
        final double tolerance = 2.0;
        
        NavigationGoal(Vec3d target) {
            this.target = target;
        }
        
        boolean isReached(ServerPlayerEntity bot) {
            return bot.getPos().distanceTo(target) <= tolerance;
        }
    }
}
```

### Advanced Pathfinding Example

```java
public class AdvancedPathfinding {
    
    public static class PathfindingStrategy implements CombatStrategy {
        
        @Override
        public String getName() {
            return "TacticalPositioning";
        }
        
        @Override
        public int getPriority() {
            return 60;
        }
        
        @Override
        public boolean canUse(ServerPlayerEntity bot, Entity target, BotSettings settings) {
            // Use when target is at medium range
            double distance = bot.distanceTo(target);
            return distance > 8.0 && distance < 20.0;
        }
        
        @Override
        public boolean execute(ServerPlayerEntity bot, Entity target, BotSettings settings, MinecraftServer server) {
            // Find tactical position
            Vec3d tacticalPos = findTacticalPosition(bot, target);
            if (tacticalPos != null) {
                moveToPosition(bot, tacticalPos);
                return true;
            }
            return false;
        }
        
        private Vec3d findTacticalPosition(ServerPlayerEntity bot, Entity target) {
            Vec3d botPos = bot.getPos();
            Vec3d targetPos = target.getPos();
            
            // Try to find high ground
            for (int y = 1; y <= 5; y++) {
                Vec3d testPos = botPos.add(0, y, 0);
                if (isValidPosition(bot, testPos) && hasLineOfSight(testPos, targetPos)) {
                    return testPos;
                }
            }
            
            // Try flanking positions
            Vec3d direction = targetPos.subtract(botPos).normalize();
            Vec3d perpendicular = new Vec3d(-direction.z, 0, direction.x);
            
            for (int side : new int[]{-1, 1}) {
                Vec3d flankPos = targetPos.add(perpendicular.multiply(side * 10));
                if (isValidPosition(bot, flankPos)) {
                    return flankPos;
                }
            }
            
            return null;
        }
        
        private boolean isValidPosition(ServerPlayerEntity bot, Vec3d pos) {
            // Check if position is safe and accessible
            World world = bot.getWorld();
            BlockPos blockPos = new BlockPos((int)pos.x, (int)pos.y, (int)pos.z);
            
            // Check if block is air and ground is solid
            return world.getBlockState(blockPos).isAir() &&
                   !world.getBlockState(blockPos.down()).isAir();
        }
        
        private boolean hasLineOfSight(Vec3d from, Vec3d to) {
            // Simplified line of sight check
            return true; // Implement proper raycast
        }
        
        private void moveToPosition(ServerPlayerEntity bot, Vec3d pos) {
            bot.teleport(pos.x, pos.y, pos.z);
        }
    }
}
```

## Retreat and Evasion

### Retreat System

```java
BotSettings settings = PvpBotAPI.getBotSettings();

// Retreat settings
boolean retreatEnabled = settings.isRetreatEnabled();
double retreatHealthPercent = settings.getRetreatHealthPercent(); // 0.1 - 0.9
double criticalHealthPercent = settings.getCriticalHealthPercent(); // 0.05 - 0.5
```

### Custom Retreat Strategy

```java
public class SmartRetreatStrategy implements CombatStrategy {
    
    @Override
    public String getName() {
        return "SmartRetreat";
    }
    
    @Override
    public int getPriority() {
        return 180; // High priority
    }
    
    @Override
    public boolean canUse(ServerPlayerEntity bot, Entity target, BotSettings settings) {
        float healthPercent = bot.getHealth() / bot.getMaxHealth();
        return healthPercent <= settings.getRetreatHealthPercent();
    }
    
    @Override
    public boolean execute(ServerPlayerEntity bot, Entity target, BotSettings settings, MinecraftServer server) {
        Vec3d safePosition = findSafeRetreatPosition(bot, target);
        if (safePosition != null) {
            // Apply speed boost
            bot.addStatusEffect(new StatusEffectInstance(
                StatusEffects.SPEED, 200, 2));
            
            // Move to safe position
            bot.teleport(safePosition.x, safePosition.y, safePosition.z);
            
            bot.sendMessage(Text.literal("§eRetreating to safety!"));
            return true;
        }
        return false;
    }
    
    private Vec3d findSafeRetreatPosition(ServerPlayerEntity bot, Entity target) {
        Vec3d botPos = bot.getPos();
        Vec3d targetPos = target.getPos();
        
        // Calculate retreat direction (away from target)
        Vec3d retreatDirection = botPos.subtract(targetPos).normalize();
        
        // Try different retreat distances
        for (double distance : new double[]{15, 20, 25, 30}) {
            Vec3d retreatPos = botPos.add(retreatDirection.multiply(distance));
            
            if (isSafePosition(bot, retreatPos, target)) {
                return retreatPos;
            }
        }
        
        return null;
    }
    
    private boolean isSafePosition(ServerPlayerEntity bot, Vec3d pos, Entity threat) {
        // Check if position is far enough from threat
        if (pos.distanceTo(threat.getPos()) < 10.0) {
            return false;
        }
        
        // Check if position is accessible
        World world = bot.getWorld();
        BlockPos blockPos = new BlockPos((int)pos.x, (int)pos.y, (int)pos.z);
        
        return world.getBlockState(blockPos).isAir() &&
               !world.getBlockState(blockPos.down()).isAir();
    }
}
```

## Group Movement

### Coordinated Movement

```java
public class GroupMovement {
    
    public static void moveBotsInFormation(List<ServerPlayerEntity> bots, Vec3d destination) {
        if (bots.isEmpty()) return;
        
        // Calculate formation positions
        List<Vec3d> positions = calculateFormationPositions(destination, bots.size());
        
        // Assign positions to bots
        for (int i = 0; i < bots.size(); i++) {
            ServerPlayerEntity bot = bots.get(i);
            Vec3d targetPos = positions.get(i);
            
            // Move bot to formation position
            moveToPosition(bot, targetPos);
        }
    }
    
    private static List<Vec3d> calculateFormationPositions(Vec3d center, int botCount) {
        List<Vec3d> positions = new ArrayList<>();
        
        if (botCount == 1) {
            positions.add(center);
            return positions;
        }
        
        // Create circular formation
        double radius = Math.max(3.0, botCount * 1.5);
        double angleStep = 2 * Math.PI / botCount;
        
        for (int i = 0; i < botCount; i++) {
            double angle = i * angleStep;
            Vec3d pos = center.add(
                Math.cos(angle) * radius,
                0,
                Math.sin(angle) * radius
            );
            positions.add(pos);
        }
        
        return positions;
    }
    
    private static void moveToPosition(ServerPlayerEntity bot, Vec3d pos) {
        // Smooth movement instead of teleportation
        Vec3d currentPos = bot.getPos();
        Vec3d direction = pos.subtract(currentPos).normalize();
        Vec3d newPos = currentPos.add(direction.multiply(0.5));
        
        bot.teleport(newPos.x, newPos.y, newPos.z);
    }
}
```

## Pathfinding Events

### Navigation Events

```java
public class NavigationTracker implements ModInitializer {
    
    @Override
    public void onInitialize() {
        // Track when bots start moving
        PvpBotAPI.getEventManager().registerTickHandler(bot -> {
            // Detect movement changes
            Vec3d velocity = bot.getVelocity();
            if (velocity.length() > 0.1) {
                // Bot is moving
                onBotMoving(bot, velocity);
            }
        });
    }
    
    private void onBotMoving(ServerPlayerEntity bot, Vec3d velocity) {
        // Custom logic for when bot is moving
        String botName = bot.getName().getString();
        
        // Example: Apply movement effects
        if (velocity.length() > 0.5) {
            // Fast movement - apply speed particles
            bot.getWorld().addParticle(
                ParticleTypes.CLOUD,
                bot.getX(), bot.getY(), bot.getZ(),
                0, 0, 0
            );
        }
    }
}
```

## Performance Considerations

### Optimizing Pathfinding

1. **Update Frequency**: Don't update paths every tick
```java
// Update pathfinding every 10 ticks (0.5 seconds)
if (bot.age % 10 == 0) {
    updatePathfinding(bot);
}
```

2. **Distance Checks**: Use squared distance for performance
```java
// Faster than using distanceTo()
double distanceSquared = bot.getPos().squaredDistanceTo(target.getPos());
if (distanceSquared < 100) { // 10 blocks
    // Close enough
}
```

3. **Batch Processing**: Process multiple bots together
```java
// Process all bots in one tick handler
PvpBotAPI.getEventManager().registerTickHandler(bot -> {
    if (bot.age % 20 == 0) { // Every second
        List<ServerPlayerEntity> allBots = getAllBots();
        processBotsInBatch(allBots);
    }
});
```

## Integration with Combat

### Combat-Aware Movement

```java
public class CombatMovementStrategy implements CombatStrategy {
    
    @Override
    public boolean execute(ServerPlayerEntity bot, Entity target, BotSettings settings, MinecraftServer server) {
        double distance = bot.distanceTo(target);
        
        // Adjust position based on weapon type
        ItemStack weapon = bot.getMainHandStack();
        
        if (weapon.getItem() == Items.BOW || weapon.getItem() == Items.CROSSBOW) {
            // Ranged weapon - maintain optimal distance
            double optimalRange = settings.getRangedOptimalRange();
            if (distance < optimalRange) {
                moveAwayFromTarget(bot, target, optimalRange - distance);
            }
        } else if (weapon.getItem() == Items.MACE) {
            // Mace - get close for maximum damage
            double maceRange = settings.getMaceRange();
            if (distance > maceRange) {
                moveTowardsTarget(bot, target, distance - maceRange);
            }
        }
        
        return true;
    }
    
    private void moveAwayFromTarget(ServerPlayerEntity bot, Entity target, double distance) {
        Vec3d direction = bot.getPos().subtract(target.getPos()).normalize();
        Vec3d newPos = bot.getPos().add(direction.multiply(distance));
        bot.teleport(newPos.x, newPos.y, newPos.z);
    }
    
    private void moveTowardsTarget(ServerPlayerEntity bot, Entity target, double distance) {
        Vec3d direction = target.getPos().subtract(bot.getPos()).normalize();
        Vec3d newPos = bot.getPos().add(direction.multiply(Math.min(distance, 3.0)));
        bot.teleport(newPos.x, newPos.y, newPos.z);
    }
}
```

The pathfinding system provides flexible navigation options for bots, from simple movement to complex tactical positioning. Use the appropriate system based on your needs and performance requirements.