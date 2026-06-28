# API Reference

Complete documentation of all PVP Bot API classes and methods.

## PvpBotAPI

Main API class for interacting with bots.

### Static Methods

#### getApiVersion()
```java
public static String getApiVersion()
```
Returns the current API version.

**Returns:** String - API version (e.g., "1.0.0")

**Example:**
```java
String version = PvpBotAPI.getApiVersion();
System.out.println("API Version: " + version);
```

#### getAllBots()
```java
public static Set<String> getAllBots()
```
Get names of all active bots.

**Returns:** `Set<String>` - immutable set of bot names

**Example:**
```java
Set<String> bots = PvpBotAPI.getAllBots();
for (String botName : bots) {
    System.out.println("Active bot: " + botName);
}
```

#### getBot(MinecraftServer, String)
```java
public static ServerPlayerEntity getBot(MinecraftServer server, String name)
```
Get bot entity by name.

**Parameters:**
- `server` - MinecraftServer instance
- `name` - bot name (case-sensitive)

**Returns:** ServerPlayerEntity or null if bot doesn't exist

**Example:**
```java
ServerPlayerEntity bot = PvpBotAPI.getBot(server, "TestBot");
if (bot != null && bot.isAlive()) {
    // Bot exists and is alive
    double health = bot.getHealth();
}
```

#### isBot(String)
```java
public static boolean isBot(String playerName)
```
Check if player is a bot.

**Parameters:**
- `playerName` - player name to check

**Returns:** boolean - true if player is a bot

**Example:**
```java
if (PvpBotAPI.isBot("TestBot")) {
    System.out.println("TestBot is a bot!");
}
```

#### getBotCount()
```java
public static int getBotCount()
```
Get number of active bots.

**Returns:** int - current bot count

#### getBotSettings()
```java
public static BotSettings getBotSettings()
```
Get bot settings singleton.

**Returns:** BotSettings - global settings instance

**Example:**
```java
BotSettings settings = PvpBotAPI.getBotSettings();
if (settings.isCombatEnabled()) {
    double range = settings.getMeleeRange();
}
```

#### getEventManager()
```java
public static BotEventManager getEventManager()
```
Get event manager singleton.

**Returns:** BotEventManager - event manager instance

#### getTotalBotsSpawned()
```java
public static int getTotalBotsSpawned()
```
Get total number of bots spawned (statistics).

**Returns:** int - total spawn count

#### getTotalBotsKilled()
```java
public static int getTotalBotsKilled()
```
Get total number of bots killed (statistics).

**Returns:** int - total kill count

---

## BotEventManager

Manager for bot lifecycle events. Singleton pattern.

### Instance Methods

#### getInstance()
```java
public static BotEventManager getInstance()
```
Get the singleton instance.

**Returns:** BotEventManager - singleton instance

#### registerSpawnHandler(BotSpawnHandler)
```java
public void registerSpawnHandler(BotSpawnHandler handler)
```
Register a bot spawn event handler.

**Parameters:**
- `handler` - functional interface: `void onBotSpawn(ServerPlayerEntity bot)`

**Example:**
```java
BotEventManager.getInstance().registerSpawnHandler(bot -> {
    System.out.println("Bot " + bot.getName().getString() + " spawned!");
});
```

#### registerDeathHandler(BotDeathHandler)
```java
public void registerDeathHandler(BotDeathHandler handler)
```
Register a bot death event handler.

**Parameters:**
- `handler` - functional interface: `void onBotDeath(ServerPlayerEntity bot)`

#### registerAttackHandler(BotAttackHandler)
```java
public void registerAttackHandler(BotAttackHandler handler)
```
Register a bot attack event handler (cancellable).

**Parameters:**
- `handler` - functional interface: `boolean onBotAttack(ServerPlayerEntity bot, Entity target)`

**Returns:** boolean - true to cancel attack, false to allow

**Example:**
```java
BotEventManager.getInstance().registerAttackHandler((bot, target) -> {
    if (target instanceof PlayerEntity player) {
        if (player.getName().getString().equals("Admin")) {
            return true; // Cancel attack on admin
        }
    }
    return false; // Allow attack
});
```

#### registerDamageHandler(BotDamageHandler)
```java
public void registerDamageHandler(BotDamageHandler handler)
```
Register a bot damage event handler (cancellable).

**Parameters:**
- `handler` - functional interface: `boolean onBotDamage(ServerPlayerEntity bot, Entity attacker, float damage)`

**Returns:** boolean - true to cancel damage, false to allow

#### registerTickHandler(BotTickHandler)
```java
public void registerTickHandler(BotTickHandler handler)
```
Register a bot tick event handler.

**Parameters:**
- `handler` - functional interface: `void onBotTick(ServerPlayerEntity bot)`

**Note:** Called every game tick for each active bot. Use sparingly for performance.

---

## CombatStrategyRegistry

Registry for custom combat strategies. Singleton pattern.

### Instance Methods

#### getInstance()
```java
public static CombatStrategyRegistry getInstance()
```
Get the singleton instance.

**Returns:** CombatStrategyRegistry - singleton instance

#### register(CombatStrategy)
```java
public void register(CombatStrategy strategy)
```
Register a combat strategy. Strategies are automatically sorted by priority (highest first).

**Parameters:**
- `strategy` - strategy implementation

**Example:**
```java
CombatStrategyRegistry.getInstance().register(new MyCustomStrategy());
```

#### unregister(CombatStrategy)
```java
public void unregister(CombatStrategy strategy)
```
Remove strategy from registry.

**Parameters:**
- `strategy` - strategy to remove

#### getStrategies()
```java
public List<CombatStrategy> getStrategies()
```
Get all registered strategies (sorted by priority).

**Returns:** `List<CombatStrategy>` - immutable list of strategies

#### clear()
```java
public void clear()
```
Remove all registered strategies.

---

## CombatStrategy Interface

Interface for custom combat strategies.

### Methods to Implement

#### getName()
```java
String getName()
```
Get strategy name for identification.

**Returns:** String - unique strategy name

#### getPriority()
```java
int getPriority()
```
Get strategy priority. Higher values execute first.

**Returns:** int - priority value (0-1000 recommended)

#### canUse(ServerPlayerEntity, Entity, BotSettings)
```java
boolean canUse(ServerPlayerEntity bot, Entity target, BotSettings settings)
```
Check if strategy can be used in current situation.

**Parameters:**
- `bot` - the bot entity
- `target` - the target entity
- `settings` - current bot settings

**Returns:** boolean - true if strategy can be used

#### execute(ServerPlayerEntity, Entity, BotSettings, MinecraftServer)
```java
boolean execute(ServerPlayerEntity bot, Entity target, BotSettings settings, MinecraftServer server)
```
Execute the combat strategy.

**Parameters:**
- `bot` - the bot entity
- `target` - the target entity
- `settings` - current bot settings
- `server` - server instance

**Returns:** boolean - true if strategy was executed successfully

**Example Implementation:**
```java
public class TeleportAttackStrategy implements CombatStrategy {
    @Override
    public String getName() {
        return "TeleportAttack";
    }
    
    @Override
    public int getPriority() {
        return 200; // High priority
    }
    
    @Override
    public boolean canUse(ServerPlayerEntity bot, Entity target, BotSettings settings) {
        return bot.hasStatusEffect(StatusEffects.INVISIBILITY) && 
               bot.distanceTo(target) > 10.0;
    }
    
    @Override
    public boolean execute(ServerPlayerEntity bot, Entity target, BotSettings settings, MinecraftServer server) {
        // Teleport behind target and attack
        Vec3d targetPos = target.getPos();
        bot.teleport(targetPos.x, targetPos.y, targetPos.z);
        bot.attack(target);
        return true;
    }
}
```

---

## BotSettings

Configuration class with 60+ settings. Singleton pattern.

### Access Methods

#### get()
```java
public static BotSettings get()
```
Get the singleton settings instance.

**Returns:** BotSettings - settings instance

### Equipment Settings

#### Auto-Equipment
```java
boolean isAutoEquipArmor()           // Auto-equip better armor
boolean isAutoEquipWeapon()          // Auto-equip better weapons
boolean isDropWorseArmor()           // Drop worse armor items
boolean isDropWorseWeapons()         // Drop worse weapon items
double getDropDistance()             // Distance to drop items (1.0-10.0)
int getDropDelay()                   // Delay between drops in ticks (1-200)
int getCheckInterval()               // Equipment check interval (1-100)
int getMinArmorLevel()               // Minimum armor level to equip (0-100)
```

### Combat Settings

#### Basic Combat
```java
boolean isCombatEnabled()            // Enable/disable combat
boolean isRevengeEnabled()           // Attack entities that damage bot
boolean isAutoTargetEnabled()        // Automatically find targets
boolean isTargetPlayers()            // Target player entities
boolean isTargetHostileMobs()        // Target hostile mobs
boolean isTargetOtherBots()          // Target other bots
double getMaxTargetDistance()        // Max targeting range (5.0-128.0)
double getMeleeRange()               // Melee attack range (2.0-6.0)
int getAttackCooldown()              // Attack cooldown in ticks (1-40)
double getMoveSpeed()                // Movement speed multiplier (0.1-2.0)
boolean isCriticalsEnabled()         // Enable critical hits
```

#### Weapon Systems
```java
boolean isRangedEnabled()            // Enable bow/crossbow combat
double getRangedMinRange()           // Min range for ranged weapons (3.0-20.0)
double getRangedOptimalRange()       // Optimal range for ranged (10.0-50.0)
int getBowMinDrawTime()              // Min bow draw time in ticks (5-30)

boolean isMaceEnabled()              // Enable mace combat
double getMaceRange()                // Mace attack range (3.0-10.0)

boolean isSpearEnabled()             // Enable spear combat
double getSpearRange()               // Spear attack range (2.0-8.0)
double getSpearChargeRange()         // Spear charge range (5.0-20.0)
int getSpearMinChargeTime()          // Min charge time (5-30)
int getSpearMaxChargeTime()          // Max charge time (20-60)

boolean isCrystalPvpEnabled()        // Enable end crystal PvP
boolean isAnchorPvpEnabled()         // Enable respawn anchor PvP
boolean isElytraMaceEnabled()        // Enable elytra+mace combat
```

#### ElytraMace Settings
```java
int getElytraMaceMaxRetries()        // Max retry attempts (1-10)
int getElytraMaceMinAltitude()       // Min altitude for attack (5-50)
double getElytraMaceAttackDistance() // Attack distance (3.0-15.0)
int getElytraMaceFireworkCount()     // Fireworks to use (1-10)
```

### Utility Settings

#### Survival
```java
boolean isAutoTotemEnabled()         // Auto-equip totems
boolean isTotemPriority()            // Prioritize totems over shields
boolean isAutoEatEnabled()           // Auto-eat food
int getMinHungerToEat()              // Min hunger to trigger eating (1-20)
boolean isAutoShieldEnabled()        // Auto-use shields
double getShieldHealthThreshold()    // Health % to use shield (0.1-1.0)
boolean isShieldBreakEnabled()       // Break enemy shields
boolean isAutoMendEnabled()          // Auto-mend equipment
double getMendDurabilityThreshold()  // Durability % to mend (0.1-0.9)
boolean isAutoPotionEnabled()        // Auto-use potions
boolean isCobwebEnabled()            // Use cobwebs tactically
```

### Navigation Settings

#### Movement
```java
boolean isUseBaritone()              // Use Baritone for pathfinding
boolean isGotoUseBaritone()          // Use Baritone for goto commands
boolean isEscortUseBaritone()        // Use Baritone for escort
boolean isFollowUseBaritone()        // Use Baritone for follow
boolean isRetreatEnabled()           // Enable tactical retreat
double getRetreatHealthPercent()     // Health % to retreat (0.1-0.9)
double getCriticalHealthPercent()    // Critical health % (0.05-0.5)
boolean isBhopEnabled()              // Enable bunny hopping
int getBhopCooldown()                // Bhop cooldown in ticks (5-30)
double getJumpBoost()                // Jump boost multiplier (0.0-0.5)
boolean isIdleWanderEnabled()        // Wander when idle
double getIdleWanderRadius()         // Wander radius (3.0-50.0)
```

### Social Settings

#### Factions
```java
boolean isFactionsEnabled()          // Enable faction system
boolean isFriendlyFireEnabled()      // Allow attacking faction members
```

#### Behavior
```java
int getMissChance()                  // Chance to miss attacks (0-100)
int getMistakeChance()               // Chance to make mistakes (0-100)
int getReactionDelay()               // Reaction delay in ticks (0-20)
boolean isBotsRelogs()               // Restore bots on server restart
boolean isUseSpecialNames()          // Use special bot names
```

#### Statistics
```java
boolean isSendStats()                // Send usage statistics
```

### Setting Modification

All settings have corresponding setter methods that automatically save to disk:

```java
BotSettings settings = BotSettings.get();
settings.setCombatEnabled(true);
settings.setMeleeRange(4.0);
settings.setAutoTargetEnabled(false);
// Settings are automatically saved
```

---

## Event Handler Interfaces

### BotSpawnHandler
```java
@FunctionalInterface
public interface BotSpawnHandler {
    void onBotSpawn(ServerPlayerEntity bot);
}
```

### BotDeathHandler
```java
@FunctionalInterface
public interface BotDeathHandler {
    void onBotDeath(ServerPlayerEntity bot);
}
```

### BotAttackHandler
```java
@FunctionalInterface
public interface BotAttackHandler {
    boolean onBotAttack(ServerPlayerEntity bot, Entity target);
}
```

### BotDamageHandler
```java
@FunctionalInterface
public interface BotDamageHandler {
    boolean onBotDamage(ServerPlayerEntity bot, Entity attacker, float damage);
}
```

### BotTickHandler
```java
@FunctionalInterface
public interface BotTickHandler {
    void onBotTick(ServerPlayerEntity bot);
}
```

---

## Error Handling

The API includes comprehensive error handling:

- **Event Handlers:** Exceptions are caught and logged, preventing cascade failures
- **Combat Strategies:** Failed strategies don't prevent other strategies from executing
- **Settings:** Invalid values are clamped to valid ranges
- **Bot Queries:** Null checks prevent crashes when bots don't exist

**Example Safe Usage:**
```java
try {
    ServerPlayerEntity bot = PvpBotAPI.getBot(server, "TestBot");
    if (bot != null && bot.isAlive()) {
        // Safe to work with bot
        double health = bot.getHealth();
    }
} catch (Exception e) {
    System.err.println("Error working with bot: " + e.getMessage());
}
```

---

## Thread Safety

- **PvpBotAPI:** All static methods are thread-safe
- **BotEventManager:** Thread-safe for registration, events fired on server thread
- **BotSettings:** Thread-safe for reading, modifications synchronized
- **CombatStrategyRegistry:** Thread-safe for registration and access

**Note:** Bot entities should only be accessed from the server thread.
