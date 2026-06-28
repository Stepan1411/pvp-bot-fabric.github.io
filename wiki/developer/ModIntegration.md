# Mod Integration

Guide for integrating PVP Bot API with other popular Minecraft mods.

## Overview

The PVP Bot API is designed to work seamlessly with other mods. This guide covers integration patterns, compatibility considerations, and specific examples for popular mods.

## General Integration Patterns

### Soft Dependencies

Use soft dependencies to integrate with mods that may not be present:

```java
public class MyBotAddon implements ModInitializer {
    
    @Override
    public void onInitialize() {
        // Core functionality
        initializeCore();
        
        // Optional integrations
        if (isModLoaded("carpet")) {
            initializeCarpetIntegration();
        }
        
        if (isModLoaded("litematica")) {
            initializeLitematicaIntegration();
        }
    }
    
    private boolean isModLoaded(String modId) {
        return FabricLoader.getInstance().isModLoaded(modId);
    }
}
```

### Conditional Class Loading

Avoid class loading errors with optional dependencies:

```java
// Create separate integration classes
public class CarpetIntegration {
    public static void initialize() {
        // Carpet-specific code here
        // This class only loads if Carpet is present
    }
}

// Load conditionally
if (isModLoaded("carpet")) {
    try {
        CarpetIntegration.initialize();
    } catch (Exception e) {
        System.err.println("Failed to initialize Carpet integration: " + e.getMessage());
    }
}
```

## Popular Mod Integrations

### Carpet Mod Integration

Carpet Mod is a dependency of PVP Bot, so it's always available:

```java
public class CarpetBotIntegration {
    
    public void initialize() {
        // Access Carpet settings
        PvpBotAPI.getEventManager().registerSpawnHandler(bot -> {
            // Example: Apply carpet-specific settings to bots
            configureCarpetSettings(bot);
        });
    }
    
    private void configureCarpetSettings(ServerPlayerEntity bot) {
        // Configure carpet settings for bot behavior
        // This is handled internally by PVP Bot
    }
}
```

### Litematica Integration

Build bots that can work with Litematica schematics:

```java
public class LitematicaBotIntegration {
    
    public void initialize() {
        PvpBotAPI.getEventManager().registerSpawnHandler(bot -> {
            // Check if bot should follow schematic
            if (shouldFollowSchematic(bot)) {
                startSchematicBuilding(bot);
            }
        });
    }
    
    private boolean shouldFollowSchematic(ServerPlayerEntity bot) {
        // Check if there's an active schematic
        // Implementation depends on Litematica API
        return false; // Placeholder
    }
    
    private void startSchematicBuilding(ServerPlayerEntity bot) {
        // Start building process
        // This would require Litematica API access
    }
}
```

### WorldEdit Integration

Bots that can work with WorldEdit selections:

```java
public class WorldEditBotIntegration {
    
    public void initialize() {
        // Register custom combat strategy for WorldEdit areas
        CombatStrategyRegistry.getInstance().register(new WorldEditAreaStrategy());
    }
    
    private class WorldEditAreaStrategy implements CombatStrategy {
        @Override
        public String getName() {
            return "WorldEditAreaProtection";
        }
        
        @Override
        public int getPriority() {
            return 200; // High priority
        }
        
        @Override
        public boolean canUse(ServerPlayerEntity bot, Entity target, BotSettings settings) {
            // Check if target is in protected WorldEdit area
            return isInProtectedArea(target.getPos());
        }
        
        @Override
        public boolean execute(ServerPlayerEntity bot, Entity target, BotSettings settings, MinecraftServer server) {
            // Don't attack in protected areas
            bot.sendMessage(Text.literal("§cCannot attack in protected area!"));
            return true; // Cancel attack
        }
        
        private boolean isInProtectedArea(Vec3d pos) {
            // Check WorldEdit regions
            // Implementation depends on WorldEdit API
            return false; // Placeholder
        }
    }
}
```

### Baritone Integration

Enhanced pathfinding with Baritone:

```java
public class BaritoneIntegration {
    
    public void initialize() {
        // Baritone is already integrated into PVP Bot
        // You can access settings through BotSettings
        
        PvpBotAPI.getEventManager().registerSpawnHandler(bot -> {
            BotSettings settings = PvpBotAPI.getBotSettings();
            
            if (settings.isUseBaritone()) {
                configureBaritoneForBot(bot);
            }
        });
    }
    
    private void configureBaritoneForBot(ServerPlayerEntity bot) {
        // Baritone configuration is handled internally
        // You can influence it through bot commands and settings
    }
}
```

### Create Mod Integration

Bots that can interact with Create contraptions:

```java
public class CreateModIntegration {
    
    public void initialize() {
        CombatStrategyRegistry.getInstance().register(new CreateContraptionStrategy());
    }
    
    private class CreateContraptionStrategy implements CombatStrategy {
        @Override
        public String getName() {
            return "CreateContraption";
        }
        
        @Override
        public int getPriority() {
            return 80;
        }
        
        @Override
        public boolean canUse(ServerPlayerEntity bot, Entity target, BotSettings settings) {
            // Check if there are Create contraptions nearby
            return hasNearbyContraptions(bot);
        }
        
        @Override
        public boolean execute(ServerPlayerEntity bot, Entity target, BotSettings settings, MinecraftServer server) {
            // Use Create contraptions tactically
            activateNearbyContraptions(bot);
            return true;
        }
        
        private boolean hasNearbyContraptions(ServerPlayerEntity bot) {
            // Check for Create mod blocks/entities
            // Implementation depends on Create API
            return false; // Placeholder
        }
        
        private void activateNearbyContraptions(ServerPlayerEntity bot) {
            // Activate contraptions
            // Implementation depends on Create API
        }
    }
}
```

### Sodium/Iris Integration

Performance optimization for rendering many bots:

```java
public class SodiumIrisIntegration {
    
    public void initialize() {
        // These mods are client-side, but you can optimize for them
        PvpBotAPI.getEventManager().registerSpawnHandler(bot -> {
            // Reduce visual effects when many bots are present
            if (PvpBotAPI.getBotCount() > 50) {
                optimizeForPerformance(bot);
            }
        });
    }
    
    private void optimizeForPerformance(ServerPlayerEntity bot) {
        // Reduce particle effects, sounds, etc.
        // This helps with client performance when using Sodium/Iris
    }
}
```

## Custom Mod Integration Example

Here's a complete example of integrating with a hypothetical "MagicMod":

```java
public class MagicModIntegration {
    
    private static final String MAGIC_MOD_ID = "magicmod";
    
    public static void initialize() {
        if (!FabricLoader.getInstance().isModLoaded(MAGIC_MOD_ID)) {
            return;
        }
        
        try {
            setupMagicIntegration();
        } catch (Exception e) {
            System.err.println("Failed to initialize MagicMod integration: " + e.getMessage());
        }
    }
    
    private static void setupMagicIntegration() {
        // Register magic-aware combat strategy
        CombatStrategyRegistry.getInstance().register(new MagicCombatStrategy());
        
        // Handle magic events
        PvpBotAPI.getEventManager().registerSpawnHandler(bot -> {
            grantMagicAbilities(bot);
        });
        
        PvpBotAPI.getEventManager().registerAttackHandler((bot, target) -> {
            // Use magic attacks
            return useMagicAttack(bot, target);
        });
    }
    
    private static void grantMagicAbilities(ServerPlayerEntity bot) {
        // Grant magic abilities to bot
        // This would use MagicMod's API
        try {
            // MagicAPI.grantAbility(bot, "fireball");
            // MagicAPI.grantAbility(bot, "heal");
        } catch (Exception e) {
            System.err.println("Failed to grant magic abilities: " + e.getMessage());
        }
    }
    
    private static boolean useMagicAttack(ServerPlayerEntity bot, Entity target) {
        // Check if bot should use magic instead of regular attack
        if (shouldUseMagic(bot, target)) {
            try {
                // MagicAPI.castSpell(bot, "fireball", target);
                return true; // Cancel regular attack
            } catch (Exception e) {
                System.err.println("Failed to cast spell: " + e.getMessage());
            }
        }
        return false; // Use regular attack
    }
    
    private static boolean shouldUseMagic(ServerPlayerEntity bot, Entity target) {
        // Decide when to use magic
        double distance = bot.distanceTo(target);
        return distance > 5.0 && distance < 20.0; // Medium range
    }
    
    private static class MagicCombatStrategy implements CombatStrategy {
        @Override
        public String getName() {
            return "MagicCombat";
        }
        
        @Override
        public int getPriority() {
            return 120; // High priority
        }
        
        @Override
        public boolean canUse(ServerPlayerEntity bot, Entity target, BotSettings settings) {
            // Check if bot has mana and magic abilities
            return hasMagicAbilities(bot) && hasSufficientMana(bot);
        }
        
        @Override
        public boolean execute(ServerPlayerEntity bot, Entity target, BotSettings settings, MinecraftServer server) {
            // Execute magic combat
            return castCombatSpell(bot, target);
        }
        
        private boolean hasMagicAbilities(ServerPlayerEntity bot) {
            // Check if bot has magic abilities
            // Implementation depends on MagicMod API
            return true; // Placeholder
        }
        
        private boolean hasSufficientMana(ServerPlayerEntity bot) {
            // Check mana levels
            // Implementation depends on MagicMod API
            return true; // Placeholder
        }
        
        private boolean castCombatSpell(ServerPlayerEntity bot, Entity target) {
            // Cast appropriate combat spell
            // Implementation depends on MagicMod API
            return true; // Placeholder
        }
    }
}
```

## Integration Best Practices

### 1. Graceful Degradation

Always handle missing dependencies gracefully:

```java
public class IntegrationManager {
    
    public void initializeIntegrations() {
        // Try each integration separately
        tryIntegration("Carpet", this::initializeCarpet);
        tryIntegration("Litematica", this::initializeLitematica);
        tryIntegration("WorldEdit", this::initializeWorldEdit);
    }
    
    private void tryIntegration(String name, Runnable integration) {
        try {
            integration.run();
            System.out.println("✓ " + name + " integration initialized");
        } catch (Exception e) {
            System.out.println("✗ " + name + " integration failed: " + e.getMessage());
        }
    }
}
```

### 2. Version Compatibility

Check mod versions when necessary:

```java
public class VersionChecker {
    
    public boolean isCompatibleVersion(String modId, String minVersion) {
        Optional<ModContainer> mod = FabricLoader.getInstance().getModContainer(modId);
        if (mod.isEmpty()) {
            return false;
        }
        
        String version = mod.get().getMetadata().getVersion().getFriendlyString();
        return compareVersions(version, minVersion) >= 0;
    }
    
    private int compareVersions(String version1, String version2) {
        // Simple version comparison
        // In practice, use a proper version comparison library
        return version1.compareTo(version2);
    }
}
```

### 3. Configuration Integration

Allow users to configure integrations:

```java
public class IntegrationConfig {
    public boolean enableCarpetIntegration = true;
    public boolean enableLitematicaIntegration = true;
    public boolean enableWorldEditIntegration = false;
    
    // Load from config file
    public static IntegrationConfig load() {
        // Implementation depends on your config system
        return new IntegrationConfig();
    }
}
```

### 4. Event Priority

Consider event execution order with other mods:

```java
// Register with appropriate priority
public void registerEvents() {
    // High priority for critical integrations
    EventPriority priority = EventPriority.HIGH;
    
    // Register with priority if supported by the mod
    // Otherwise, register early in initialization
}
```

## Testing Integrations

### Unit Testing

Test integrations with mock objects:

```java
public class IntegrationTest {
    
    @Test
    public void testMagicIntegration() {
        // Mock bot and target
        ServerPlayerEntity mockBot = createMockBot();
        Entity mockTarget = createMockTarget();
        
        // Test integration
        MagicCombatStrategy strategy = new MagicCombatStrategy();
        boolean canUse = strategy.canUse(mockBot, mockTarget, BotSettings.get());
        
        assertTrue(canUse);
    }
}
```

### Integration Testing

Test with actual mod combinations:

```java
public class IntegrationTestSuite {
    
    @Test
    public void testWithCarpetMod() {
        // Test PVP Bot + Carpet integration
        assumeTrue(isModLoaded("carpet"));
        
        // Run integration tests
    }
    
    @Test
    public void testWithLitematica() {
        // Test PVP Bot + Litematica integration
        assumeTrue(isModLoaded("litematica"));
        
        // Run integration tests
    }
}
```

## Common Integration Challenges

### 1. Class Loading Issues

**Problem:** NoClassDefFoundError when optional mod is missing.

**Solution:** Use reflection or separate integration classes:

```java
// Safe integration loading
try {
    Class<?> integrationClass = Class.forName("com.example.MyIntegration");
    Method initMethod = integrationClass.getMethod("initialize");
    initMethod.invoke(null);
} catch (ClassNotFoundException e) {
    // Mod not present, skip integration
} catch (Exception e) {
    System.err.println("Integration failed: " + e.getMessage());
}
```

### 2. API Changes

**Problem:** Integrated mod changes its API.

**Solution:** Version-specific integration:

```java
public class VersionedIntegration {
    
    public void initialize() {
        String version = getModVersion("targetmod");
        
        if (version.startsWith("1.0")) {
            initializeV1();
        } else if (version.startsWith("2.0")) {
            initializeV2();
        } else {
            System.err.println("Unsupported mod version: " + version);
        }
    }
}
```

### 3. Event Conflicts

**Problem:** Multiple mods handling the same events.

**Solution:** Coordinate with other mods:

```java
// Check if other mods are handling the event
public boolean shouldHandleEvent(ServerPlayerEntity bot) {
    // Check for other mod markers
    if (bot.getDataTracker().get(OTHER_MOD_MARKER)) {
        return false; // Let other mod handle
    }
    return true;
}
```

## Documentation

When creating integrations, document:

1. **Required mod versions**
2. **Optional vs required dependencies**
3. **Configuration options**
4. **Known conflicts**
5. **Usage examples**

Example README section:

```markdown
## Mod Integrations

### Supported Mods

- **Carpet Mod** (Required) - Core functionality
- **Litematica** (Optional) - Schematic building support
- **WorldEdit** (Optional) - Region protection
- **Create** (Optional) - Contraption interaction

### Configuration

```json
{
  "integrations": {
    "litematica": true,
    "worldedit": false,
    "create": true
  }
}
```

### Known Issues

- WorldEdit integration requires WorldEdit 7.2.0+
- Create integration may conflict with Create: Extended
```

Integration with other mods expands the possibilities for bot behavior and creates richer gameplay experiences. Always prioritize compatibility and graceful degradation to ensure your addon works well in diverse mod environments.