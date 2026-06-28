# Quick Start Guide

Get started with PVP Bot API in minutes!

## Prerequisites

- **Minecraft:** 1.21.11+
- **Fabric Loader:** 0.16.0+
- **Java:** 21+
- **PVP Bot Fabric:** Latest version

## Step 1: Add Dependency

Add PVP Bot as a dependency in your `build.gradle`:

```gradle
repositories {
    maven { url 'https://jitpack.io' }
}

dependencies {
    modImplementation "com.github.Stepan1411:pvp-bot-fabric:VERSION"
}
```

Replace `VERSION` with the latest version: [![](https://jitpack.io/v/Stepan1411/pvp-bot-fabric.svg)](https://jitpack.io/#Stepan1411/pvp-bot-fabric)

## Step 2: Declare Dependency

Add to your `fabric.mod.json`:

```json
{
  "depends": {
    "pvp-bot-fabric": "*"
  }
}
```

## Step 3: Create Your Mod

Create your main mod class:

```java
package com.example.mybotaddon;

import net.fabricmc.api.ModInitializer;
import org.stepan1411.pvp_bot.api.PvpBotAPI;
import org.stepan1411.pvp_bot.api.event.BotEventManager;

public class MyBotAddon implements ModInitializer {
    @Override
    public void onInitialize() {
        System.out.println("MyBotAddon initializing...");
        
        // Get the event manager
        BotEventManager eventManager = PvpBotAPI.getEventManager();
        
        // Register a simple spawn handler
        eventManager.registerSpawnHandler(bot -> {
            System.out.println("Bot spawned: " + bot.getName().getString());
        });
        
        System.out.println("MyBotAddon initialized!");
    }
}
```

## Step 4: Test Your Addon

1. Build your mod: `./gradlew build`
2. Place the JAR in your mods folder
3. Start Minecraft with Fabric
4. Spawn a bot: `/pvpbot spawn TestBot`
5. Check console for your message!

## Common Use Cases

### 1. Bot Statistics Tracker

```java
public class BotStatsTracker implements ModInitializer {
    private final Map<String, Integer> killCounts = new HashMap<>();
    
    @Override
    public void onInitialize() {
        BotEventManager manager = PvpBotAPI.getEventManager();
        
        // Track kills
        manager.registerAttackHandler((bot, target) -> {
            if (target.isDead()) {
                String botName = bot.getName().getString();
                int kills = killCounts.getOrDefault(botName, 0) + 1;
                killCounts.put(botName, kills);
                
                System.out.println(botName + " now has " + kills + " kills!");
            }
            return false; // Don't cancel attack
        });
        
        // Reset stats on death
        manager.registerDeathHandler(bot -> {
            killCounts.remove(bot.getName().getString());
        });
    }
}
```

### 2. Custom Combat Strategy

```java
import org.stepan1411.pvp_bot.api.combat.CombatStrategy;
import org.stepan1411.pvp_bot.api.combat.CombatStrategyRegistry;
import org.stepan1411.pvp_bot.bot.BotSettings;

public class TeleportStrategy implements CombatStrategy {
    @Override
    public String getName() {
        return "TeleportAttack";
    }
    
    @Override
    public int getPriority() {
        return 150; // Higher than default strategies
    }
    
    @Override
    public boolean canUse(ServerPlayerEntity bot, Entity target, BotSettings settings) {
        // Only use if bot has ender pearls and target is far
        return bot.getInventory().contains(Items.ENDER_PEARL) && 
               bot.distanceTo(target) > 10.0;
    }
    
    @Override
    public boolean execute(ServerPlayerEntity bot, Entity target, BotSettings settings, MinecraftServer server) {
        // Find ender pearl in inventory
        for (int i = 0; i < bot.getInventory().size(); i++) {
            ItemStack stack = bot.getInventory().getStack(i);
            if (stack.getItem() == Items.ENDER_PEARL) {
                // Use ender pearl
                bot.setStackInHand(Hand.MAIN_HAND, stack);
                bot.interactItem(Hand.MAIN_HAND);
                return true;
            }
        }
        return false;
    }
}

// Register in your mod initializer:
public class MyMod implements ModInitializer {
    @Override
    public void onInitialize() {
        CombatStrategyRegistry.getInstance().register(new TeleportStrategy());
    }
}
```

### 3. Bot Protection System

```java
public class BotProtection implements ModInitializer {
    private final Set<String> protectedBots = new HashSet<>();
    
    @Override
    public void onInitialize() {
        BotEventManager manager = PvpBotAPI.getEventManager();
        
        // Protect bots with low health
        manager.registerDamageHandler((bot, attacker, damage) -> {
            String botName = bot.getName().getString();
            
            // Enable protection at low health
            if (bot.getHealth() <= 4.0f) {
                protectedBots.add(botName);
                bot.sendMessage(Text.literal("§eProtection activated!"));
                return true; // Cancel damage
            }
            
            // Disable protection at high health
            if (bot.getHealth() >= 15.0f && protectedBots.contains(botName)) {
                protectedBots.remove(botName);
                bot.sendMessage(Text.literal("§aProtection deactivated!"));
            }
            
            return protectedBots.contains(botName);
        });
    }
}
```

## API Overview

### Core Classes

- **`PvpBotAPI`** - Main API entry point
- **`BotEventManager`** - Event system
- **`CombatStrategyRegistry`** - Combat strategy system
- **`BotSettings`** - Configuration access

### Key Methods

```java
// Bot queries
Set<String> bots = PvpBotAPI.getAllBots();
boolean isBot = PvpBotAPI.isBot("PlayerName");
ServerPlayerEntity bot = PvpBotAPI.getBot(server, "BotName");

// Statistics
int count = PvpBotAPI.getBotCount();
int spawned = PvpBotAPI.getTotalBotsSpawned();
int killed = PvpBotAPI.getTotalBotsKilled();

// Configuration
BotSettings settings = PvpBotAPI.getBotSettings();
boolean combatEnabled = settings.isCombatEnabled();

// Events
BotEventManager events = PvpBotAPI.getEventManager();
events.registerSpawnHandler(bot -> { /* ... */ });
```

## Next Steps

1. **[API Reference](APIReference.md)** - Complete method documentation
2. **[Events](Events.md)** - Detailed event system guide
3. **[Combat Strategies](CombatStrategies.md)** - Custom combat logic
4. **[Examples](Examples.md)** - More code examples
5. **[Best Practices](BestPractices.md)** - Optimization tips

## Troubleshooting

### Common Issues

**Bot not found:**
```java
ServerPlayerEntity bot = PvpBotAPI.getBot(server, "BotName");
if (bot == null) {
    System.out.println("Bot doesn't exist or isn't loaded");
}
```

**Event not firing:**
- Make sure bot is actually spawned with `/pvpbot spawn BotName`
- Check console for error messages
- Verify your mod is loading correctly

**Combat strategy not working:**
- Check `canUse()` method returns true
- Verify priority is high enough
- Make sure strategy is registered in `onInitialize()`

### Debug Tips

```java
// Check API version
System.out.println("API Version: " + PvpBotAPI.getApiVersion());

// List all bots
System.out.println("Active bots: " + PvpBotAPI.getAllBots());

// Check bot settings
BotSettings settings = PvpBotAPI.getBotSettings();
System.out.println("Combat enabled: " + settings.isCombatEnabled());
```

## Example Project Structure

```
src/main/java/com/example/mybotaddon/
├── MyBotAddon.java              # Main mod class
├── events/
│   ├── BotStatsTracker.java     # Event handlers
│   └── BotProtection.java
├── strategies/
│   ├── TeleportStrategy.java    # Combat strategies
│   └── HealingStrategy.java
└── utils/
    └── BotUtils.java            # Utility methods
```

Ready to build something awesome? Check out the [Examples](Examples.md) for more inspiration!