# PVP Bot API - Developer Documentation

## ⚠️ WARNING ⚠️ 
API is stable but some advanced features may change in future versions.

Welcome to the PVP Bot Fabric API documentation! This comprehensive API allows you to create powerful addons and extensions for the mod.

## 📚 Contents

- [🚀 Quick Start](QuickStart.md) - start here
- [🏗️ API Structure](APIStructure.md) - architecture overview
- [📖 API Reference](APIReference.md) - complete method documentation
- [⚡ Events](Events.md) - event system
- [🗺️ Pathfinding](Pathfinding.md) - bot navigation and pathfinding
- [⚔️ Combat Strategies](CombatStrategies.md) - custom combat logic
- [💡 Examples](Examples.md) - ready-to-use code examples
- [🔌 Mod Integration](ModIntegration.md) - working with other mods
- [✨ Best Practices](BestPractices.md) - recommendations
- [❓ FAQ](FAQ.md) - frequently asked questions

## 🎯 API Features

### Bot Lifecycle Events
- **Spawn** - when bot spawns in world
- **Death** - when bot dies or is removed
- **Attack** - when bot attacks entity (cancellable)
- **Damage** - when bot takes damage (cancellable)
- **Tick** - every game tick for each bot

### Combat System
- **Custom Strategies** - priority-based combat behaviors
- **Weapon Systems** - melee, ranged, mace, spear, crystal PvP, anchor PvP
- **ElytraMace** - aerial combat with elytra and mace
- **Auto-Equipment** - automatic armor and weapon management

### Bot Management
- **Query System** - get bot lists, check bot status
- **Statistics** - spawn/kill counters, performance metrics
- **Configuration** - access to 60+ bot settings
- **Faction System** - team-based bot management

## 📦 Installation

Add dependency to your `build.gradle`:
[![](https://jitpack.io/v/Stepan1411/pvp-bot-fabric.svg)](https://jitpack.io/#Stepan1411/pvp-bot-fabric)

```gradle
repositories {
    maven { url 'https://jitpack.io' }
}

dependencies {
    modImplementation "com.github.Stepan1411:pvp-bot-fabric:VERSION"
}
```

## 🚀 Quick Example

```java
import org.stepan1411.pvp_bot.api.PvpBotAPI;
import org.stepan1411.pvp_bot.api.event.BotEventManager;
import org.stepan1411.pvp_bot.api.combat.CombatStrategy;
import org.stepan1411.pvp_bot.api.combat.CombatStrategyRegistry;

public class MyAddon implements ModInitializer {
    @Override
    public void onInitialize() {
        // Register event handlers
        BotEventManager eventManager = PvpBotAPI.getEventManager();
        
        // Bot spawn event
        eventManager.registerSpawnHandler(bot -> {
            System.out.println("Bot spawned: " + bot.getName().getString());
        });
        
        // Bot attack event (cancellable)
        eventManager.registerAttackHandler((bot, target) -> {
            System.out.println(bot.getName().getString() + " attacks " + target.getName().getString());
            return false; // false = don't cancel attack
        });
        
        // Bot damage event (cancellable)
        eventManager.registerDamageHandler((bot, attacker, damage) -> {
            if (damage > 10.0f) {
                System.out.println("High damage detected: " + damage);
                return true; // true = cancel damage
            }
            return false;
        });
        
        // Register custom combat strategy
        CombatStrategyRegistry.getInstance().register(new MyCustomStrategy());
    }
}

// Custom combat strategy example
class MyCustomStrategy implements CombatStrategy {
    @Override
    public String getName() {
        return "MyCustomStrategy";
    }
    
    @Override
    public int getPriority() {
        return 100; // Higher priority = executed first
    }
    
    @Override
    public boolean canUse(ServerPlayerEntity bot, Entity target, BotSettings settings) {
        // Check if strategy can be used
        return target instanceof PlayerEntity && bot.getHealth() > 10.0f;
    }
    
    @Override
    public boolean execute(ServerPlayerEntity bot, Entity target, BotSettings settings, MinecraftServer server) {
        // Execute custom combat logic
        System.out.println("Executing custom strategy!");
        return true; // true = strategy was executed
    }
}
```

## 🔧 Advanced Features

### Bot Statistics
```java
// Get bot statistics
int totalBots = PvpBotAPI.getBotCount();
int totalSpawned = PvpBotAPI.getTotalBotsSpawned();
int totalKilled = PvpBotAPI.getTotalBotsKilled();
Set<String> activeBots = PvpBotAPI.getAllBots();
```

### Configuration Access
```java
// Access bot settings
BotSettings settings = PvpBotAPI.getBotSettings();
boolean combatEnabled = settings.isCombatEnabled();
double meleeRange = settings.getMeleeRange();
boolean crystalPvpEnabled = settings.isCrystalPvpEnabled();
```

### Bot Queries
```java
// Check if player is a bot
boolean isBot = PvpBotAPI.isBot("PlayerName");

// Get bot entity
ServerPlayerEntity bot = PvpBotAPI.getBot(server, "BotName");
if (bot != null && bot.isAlive()) {
    // Work with bot entity
}
```

## 📖 Additional Information

- [GitHub Repository](https://github.com/Stepan1411/pvp-bot-fabric)
- [Issues](https://github.com/Stepan1411/pvp-bot-fabric/issues)
- [Modrinth](https://modrinth.com/mod/pvp-bot-fabric)

## 📝 API Version

Current API version: [![](https://jitpack.io/v/Stepan1411/pvp-bot-fabric.svg)](https://jitpack.io/#Stepan1411/pvp-bot-fabric)

Check version programmatically:
```java
String version = PvpBotAPI.getApiVersion();
```
