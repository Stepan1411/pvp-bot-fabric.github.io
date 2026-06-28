# FAQ - Frequently Asked Questions

## General Questions

### What Minecraft version is supported?

API works with Minecraft 1.21.11+ and Fabric Loader 0.16.0+. Java 21+ is required.

### Do I need additional mods?

Only PVP Bot Fabric and Carpet Mod (PVP Bot dependency). The API is included in PVP Bot Fabric.

### Can I use the API on a server?

Yes, the API works on both client and server. Server-side usage is recommended for multiplayer environments.

### What's the current API version?

Check programmatically: `PvpBotAPI.getApiVersion()` or see the latest release on [JitPack](https://jitpack.io/#Stepan1411/pvp-bot-fabric).

## Development

### How do I start developing an addon?

1. Read [Quick Start Guide](QuickStart.md)
2. Study [Examples](Examples.md)
3. Set up your development environment
4. Create your first event handler

### Where can I find code examples?

- [Examples](Examples.md) in documentation
- [Complete Example Mod](https://github.com/Stepan1411/pvpbot-example-mod)
- [Main Repository](https://github.com/Stepan1411/pvp-bot-fabric)

### How do I debug my addon?

```java
// Add logging
private static final Logger LOGGER = LoggerFactory.getLogger("myaddon");

@Override
public void onInitialize() {
    LOGGER.info("My addon loaded");
    
    PvpBotAPI.getEventManager().registerSpawnHandler(bot -> {
        LOGGER.debug("Bot spawned: {}", bot.getName().getString());
    });
}
```

Run with debug flags: `-Dmyaddon.debug=true`

### How do I check if PVP Bot is loaded?

```java
public boolean isPvpBotLoaded() {
    try {
        Class.forName("org.stepan1411.pvp_bot.api.PvpBotAPI");
        return true;
    } catch (ClassNotFoundException e) {
        return false;
    }
}
```

## Events

### How do I cancel a bot attack?

```java
PvpBotAPI.getEventManager().registerAttackHandler((bot, target) -> {
    if (shouldCancelAttack(target)) {
        return true; // true = cancel attack
    }
    return false; // false = allow attack
});
```

### How do I cancel bot damage?

```java
PvpBotAPI.getEventManager().registerDamageHandler((bot, attacker, damage) -> {
    if (damage > 15.0f) {
        return true; // Cancel high damage
    }
    return false; // Allow normal damage
});
```

### How often is BotTickHandler called?

20 times per second (every game tick). Use modulo to reduce frequency:

```java
registerTickHandler(bot -> {
    if (bot.age % 20 == 0) { // Once per second
        // Your code here
    }
    
    if (bot.age % 100 == 0) { // Once every 5 seconds
        // Less frequent operations
    }
});
```

### Can I change handler execution order?

Handlers execute in registration order. Register important handlers first. For cancellable events, all handlers are called regardless of cancellation.

### Do events work with all bots?

Yes, events work with all bots managed by PVP Bot, including those spawned by other mods or restored from saves.

## Combat Strategies

### How do I set strategy priority?

```java
@Override
public int getPriority() {
    return 150; // Higher = executes earlier
}
```

**Priority Ranges:**
- **200+** - Critical (escape, emergency healing)
- **150-199** - High priority combat (Crystal PvP, Anchor PvP)
- **100-149** - Combat preparation (buffs, positioning)
- **50-99** - Special attacks (weapon abilities)
- **1-49** - Basic combat (melee, ranged)

### How does cooldown work?

```java
@Override
public int getCooldown() {
    return 100; // 100 ticks = 5 seconds
}
```

Strategy won't be used again until cooldown expires. Cooldown is per-strategy, not per-bot.

### Can I use multiple strategies simultaneously?

Strategies execute by priority order. The first strategy where `canUse()` returns `true` and `execute()` returns `true` will be used. Other strategies are skipped for that combat tick.

### Why isn't my strategy being called?

1. **Check registration**: Ensure you called `CombatStrategyRegistry.getInstance().register(strategy)`
2. **Check canUse()**: Add logging to see if conditions are met
3. **Check priority**: Higher priority strategies execute first
4. **Check cooldown**: Strategy may be on cooldown
5. **Check combat settings**: Bot combat must be enabled

```java
// Debug your strategy
@Override
public boolean canUse(ServerPlayerEntity bot, Entity target, BotSettings settings) {
    boolean result = /* your conditions */;
    System.out.println("Strategy " + getName() + " canUse: " + result);
    return result;
}
```

### How do I access bot inventory in strategies?

```java
@Override
public boolean execute(ServerPlayerEntity bot, Entity target, BotSettings settings, MinecraftServer server) {
    // Check for items
    boolean hasSword = bot.getInventory().contains(Items.DIAMOND_SWORD);
    
    // Count items
    int appleCount = bot.getInventory().count(Items.GOLDEN_APPLE);
    
    // Find item slot
    for (int i = 0; i < bot.getInventory().size(); i++) {
        ItemStack stack = bot.getInventory().getStack(i);
        if (stack.getItem() == Items.TOTEM_OF_UNDYING) {
            // Found totem at slot i
            break;
        }
    }
    
    return true;
}
```

## Performance

### My handler is lagging the game. What should I do?

1. **Reduce execution frequency:**
```java
// Instead of every tick
registerTickHandler(bot -> {
    if (bot.age % 100 == 0) { // Once every 5 seconds
        heavyOperation(bot);
    }
});
```

2. **Use caching:**
```java
private final Map<String, CachedData> cache = new HashMap<>();

registerTickHandler(bot -> {
    String botName = bot.getName().getString();
    CachedData data = cache.get(botName);
    
    if (data == null || data.isExpired()) {
        data = computeExpensiveData(bot);
        cache.put(botName, data);
    }
    
    // Use cached data
});
```

3. **Optimize algorithms and use efficient data structures**

### How many bots can the API handle?

The API is optimized for hundreds of bots. Actual limit depends on:
- Your hardware
- Complexity of your event handlers
- Number of active strategies
- Server tick rate

### How do I profile my addon performance?

```java
public class PerformanceProfiler {
    private final Map<String, Long> timings = new HashMap<>();
    
    public void startTiming(String operation) {
        timings.put(operation, System.nanoTime());
    }
    
    public void endTiming(String operation) {
        Long start = timings.get(operation);
        if (start != null) {
            long duration = System.nanoTime() - start;
            System.out.println(operation + " took: " + (duration / 1_000_000) + "ms");
        }
    }
}
```

### Should I use async operations in event handlers?

**Be careful with async operations:**

```java
// WRONG - can cause race conditions
registerSpawnHandler(bot -> {
    CompletableFuture.runAsync(() -> {
        bot.setHealth(20.0f); // Dangerous - not on server thread!
    });
});

// CORRECT - schedule on server thread
registerSpawnHandler(bot -> {
    CompletableFuture.runAsync(() -> {
        // Do heavy computation
        String result = heavyComputation();
        
        // Schedule result handling on server thread
        bot.getServer().execute(() -> {
            handleResult(bot, result);
        });
    });
});
```

## Compatibility

### Does the API work with other mods?

Yes! The API is designed to be compatible with other mods. See [Mod Integration](ModIntegration.md) for examples.

### What if my mod conflicts with another?

1. **Check dependency versions** in `fabric.mod.json`
2. **Use soft dependencies** for optional integrations
3. **Handle exceptions** gracefully
4. **Test with common mod combinations**

### How do I check if another mod is installed?

```java
// Method 1: Class loading
public boolean isModInstalled(String className) {
    try {
        Class.forName(className);
        return true;
    } catch (ClassNotFoundException e) {
        return false;
    }
}

// Method 2: Fabric Loader API
public boolean isModLoaded(String modId) {
    return FabricLoader.getInstance().isModLoaded(modId);
}

// Usage
if (isModLoaded("carpet")) {
    // Carpet mod is installed
    setupCarpetIntegration();
}
```

### How do I handle version compatibility?

```java
public void checkApiCompatibility() {
    String apiVersion = PvpBotAPI.getApiVersion();
    String[] parts = apiVersion.split("\\.");
    int major = Integer.parseInt(parts[0]);
    int minor = Integer.parseInt(parts[1]);
    
    if (major < 1 || (major == 1 && minor < 2)) {
        System.err.println("Warning: Your addon requires API 1.2+, found: " + apiVersion);
    }
}
```

### Can I use the API with Quilt?

The API is designed for Fabric, but may work with Quilt due to compatibility. Testing is recommended.

## Common Errors & Solutions

### "Cannot find symbol: PvpBotAPI"

**Problem:** Compilation error when trying to use PvpBotAPI.

**Solution:** Add the dependency to your `build.gradle`:

```gradle
repositories {
    maven { url 'https://jitpack.io' }
}

dependencies {
    modImplementation "com.github.Stepan1411:pvp-bot-fabric:VERSION"
}
```

And declare the dependency in `fabric.mod.json`:

```json
{
  "depends": {
    "pvp-bot-fabric": "*"
  }
}
```

### "NoSuchMethodError" at runtime

**Problem:** Method exists at compile time but not at runtime.

**Solution:** API version mismatch. Update to the latest version:

```gradle
dependencies {
    modImplementation "com.github.Stepan1411:pvp-bot-fabric:+" // Latest version
}
```

### Bot doesn't respond to my events

**Problem:** Event handlers are registered but never called.

**Solutions:**

1. **Verify handler registration:**
```java
@Override
public void onInitialize() {
    System.out.println("Registering event handlers...");
    
    PvpBotAPI.getEventManager().registerSpawnHandler(bot -> {
        System.out.println("Spawn handler called for: " + bot.getName().getString());
    });
    
    System.out.println("Event handlers registered!");
}
```

2. **Check bot exists:**
```java
Set<String> bots = PvpBotAPI.getAllBots();
System.out.println("Active bots: " + bots);
```

3. **Verify conditions:**
```java
registerAttackHandler((bot, target) -> {
    System.out.println("Attack event: " + bot.getName().getString() + " -> " + target.getName().getString());
    return false;
});
```

### Combat Strategy not executing

**Problem:** Strategy is registered but `canUse()` and `execute()` are never called.

**Solutions:**

1. **Check combat is enabled:**
```java
BotSettings settings = PvpBotAPI.getBotSettings();
if (!settings.isCombatEnabled()) {
    System.out.println("Combat is disabled!");
}
```

2. **Verify strategy registration:**
```java
CombatStrategyRegistry registry = CombatStrategyRegistry.getInstance();
registry.register(myStrategy);

List<CombatStrategy> strategies = registry.getStrategies();
System.out.println("Registered strategies: " + strategies.size());
```

3. **Debug canUse() method:**
```java
@Override
public boolean canUse(ServerPlayerEntity bot, Entity target, BotSettings settings) {
    boolean result = /* your conditions */;
    System.out.println("Strategy " + getName() + " canUse: " + result);
    return result;
}
```

### "Cannot resolve method getServer()"

**Problem:** Documentation shows `bot.getServer()` but method doesn't exist.

**Solution:** Use the server parameter or get from world:

```java
// WRONG:
MinecraftServer server = bot.getServer(); // Doesn't exist

// CORRECT - use parameter:
@Override
public boolean execute(ServerPlayerEntity bot, Entity target, BotSettings settings, MinecraftServer server) {
    // server parameter is available
}

// CORRECT - get from world:
ServerWorld world = (ServerWorld) bot.getEntityWorld();
MinecraftServer server = world.getServer();
```

### BotAttackHandler not cancelling attacks

**Problem:** Returning `true` from attack handler doesn't cancel the attack.

**Solution:** This should work in current versions. Verify your handler:

```java
PvpBotAPI.getEventManager().registerAttackHandler((bot, target) -> {
    System.out.println("Attack handler called");
    
    if (shouldCancelAttack(bot, target)) {
        System.out.println("Cancelling attack");
        return true; // This should cancel the attack
    }
    
    System.out.println("Allowing attack");
    return false;
});
```

### Memory leaks with bot data

**Problem:** Bot data accumulates and never gets cleaned up.

**Solution:** Always clean up on bot death:

```java
private final Map<String, BotData> botData = new HashMap<>();

@Override
public void onInitialize() {
    // Store data on spawn
    PvpBotAPI.getEventManager().registerSpawnHandler(bot -> {
        botData.put(bot.getName().getString(), new BotData());
    });
    
    // IMPORTANT: Clean up on death
    PvpBotAPI.getEventManager().registerDeathHandler(bot -> {
        botData.remove(bot.getName().getString());
    });
}
```

### ClassCastException with bot entities

**Problem:** Casting player to ServerPlayerEntity fails.

**Solution:** Always check before casting:

```java
// WRONG:
ServerPlayerEntity bot = (ServerPlayerEntity) player; // May fail

// CORRECT:
if (player instanceof ServerPlayerEntity serverPlayer) {
    // Safe to use serverPlayer
} else {
    System.err.println("Player is not a ServerPlayerEntity: " + player.getClass());
}
```

## Publishing & Distribution

### How do I publish my addon?

1. **Create GitHub repository** with your addon code
2. **Publish on mod platforms:**
   - [Modrinth](https://modrinth.com/) (recommended)
   - [CurseForge](https://www.curseforge.com/)
3. **Include proper metadata:**
   - README with installation instructions
   - Screenshots/GIFs of functionality
   - Clear dependency requirements
   - License information

### What should I include in fabric.mod.json?

```json
{
  "schemaVersion": 1,
  "id": "your-addon-id",
  "version": "1.0.0",
  "name": "Your Addon Name",
  "description": "Description of your addon",
  "authors": ["YourName"],
  "contact": {
    "homepage": "https://github.com/yourusername/your-addon",
    "sources": "https://github.com/yourusername/your-addon",
    "issues": "https://github.com/yourusername/your-addon/issues"
  },
  "license": "MIT",
  "icon": "assets/your-addon/icon.png",
  "environment": "*",
  "entrypoints": {
    "main": ["com.yourname.youraddon.YourAddon"]
  },
  "depends": {
    "fabricloader": ">=0.16.0",
    "minecraft": ">=1.21.11",
    "java": ">=21",
    "pvp-bot-fabric": "*"
  }
}
```

### Do I need a license?

**Yes, recommended licenses:**
- **MIT** - Simple and permissive
- **Apache 2.0** - More detailed, includes patent protection
- **GPL-3.0** - Copyleft license

### How do I version my addon?

Use [Semantic Versioning](https://semver.org/):
- **MAJOR.MINOR.PATCH** (e.g., 1.2.3)
- **MAJOR** - Breaking changes
- **MINOR** - New features (backward compatible)
- **PATCH** - Bug fixes

### Should I include example code?

Yes! Include:
- `examples/` directory with sample implementations
- Detailed README with usage examples
- JavaDoc comments on public APIs
- Wiki or documentation site for complex addons

## Support & Community

### Where can I get help?

- **GitHub Issues**: [Report bugs and ask questions](https://github.com/Stepan1411/pvp-bot-fabric/issues)
- **GitHub Discussions**: [Community discussions](https://github.com/Stepan1411/pvp-bot-fabric/discussions)
- **Documentation**: [Complete API documentation](Home.md)

### How do I report a bug?

1. **Search existing issues** to avoid duplicates
2. **Create detailed issue** with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Minecraft/Fabric/API versions
   - Relevant code snippets
   - Log files if applicable

### Can I contribute to the API?

**Yes! Contributions are welcome:**

1. **Fork the repository**
2. **Create feature branch**: `git checkout -b feature/amazing-feature`
3. **Write tests** for new functionality
4. **Follow code style** of existing code
5. **Submit pull request** with clear description

**Types of contributions:**
- Bug fixes
- New API features
- Documentation improvements
- Example code
- Performance optimizations

### How do I request a new feature?

1. **Check existing issues** for similar requests
2. **Create feature request** with:
   - Clear use case description
   - Proposed API design
   - Example usage code
   - Benefits to the community

### Is there a community Discord/forum?

Check the [main repository](https://github.com/Stepan1411/pvp-bot-fabric) for current community links and announcements.

## Licensing

### What license is the API under?

See LICENSE file in repository.

### Can I use the API in commercial projects?

Yes, if allowed by the license.
