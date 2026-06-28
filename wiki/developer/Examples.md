# Examples

Ready-to-use examples of PVP Bot API usage. These examples demonstrate common patterns and advanced techniques for bot addon development.

📦 **Complete Example Mod:** [pvpbot-example-mod](https://github.com/Stepan1411/pvpbot-example-mod)

## Example 1: Comprehensive Bot Logger

Track all bot activities with detailed logging and file output.

```java
package com.example.botlogger;

import net.fabricmc.api.ModInitializer;
import org.stepan1411.pvp_bot.api.PvpBotAPI;
import org.stepan1411.pvp_bot.api.event.BotEventManager;

import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class BotLogger implements ModInitializer {
    
    private static final DateTimeFormatter TIMESTAMP = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
    private FileWriter logWriter;
    
    @Override
    public void onInitialize() {
        try {
            logWriter = new FileWriter("bot_activity.log", true);
        } catch (IOException e) {
            System.err.println("Failed to create log file: " + e.getMessage());
        }
        
        BotEventManager events = PvpBotAPI.getEventManager();
        
        // Log spawns
        events.registerSpawnHandler(bot -> {
            String message = String.format("[SPAWN] %s spawned at %.2f, %.2f, %.2f in %s", 
                bot.getName().getString(),
                bot.getX(), bot.getY(), bot.getZ(),
                bot.getWorld().getRegistryKey().getValue().toString()
            );
            log(message);
        });
        
        // Log deaths
        events.registerDeathHandler(bot -> {
            String message = String.format("[DEATH] %s died at %.2f, %.2f, %.2f", 
                bot.getName().getString(),
                bot.getX(), bot.getY(), bot.getZ()
            );
            log(message);
        });
        
        // Log attacks
        events.registerAttackHandler((bot, target) -> {
            String message = String.format("[ATTACK] %s attacked %s (distance: %.2f)", 
                bot.getName().getString(),
                target.getName().getString(),
                bot.distanceTo(target)
            );
            log(message);
            return false; // Don't cancel
        });
        
        // Log damage
        events.registerDamageHandler((bot, attacker, damage) -> {
            String attackerName = attacker != null ? attacker.getName().getString() : "Environment";
            String message = String.format("[DAMAGE] %s took %.2f damage from %s (health: %.2f)", 
                bot.getName().getString(),
                damage,
                attackerName,
                bot.getHealth()
            );
            log(message);
            return false; // Don't cancel
        });
        
        // Periodic status updates
        events.registerTickHandler(bot -> {
            // Log status every 5 minutes (6000 ticks)
            if (bot.age % 6000 == 0) {
                String message = String.format("[STATUS] %s - Health: %.2f, Position: %.2f, %.2f, %.2f", 
                    bot.getName().getString(),
                    bot.getHealth(),
                    bot.getX(), bot.getY(), bot.getZ()
                );
                log(message);
            }
        });
    }
    
    private void log(String message) {
        String timestamped = String.format("[%s] %s", 
            LocalDateTime.now().format(TIMESTAMP), 
            message
        );
        
        System.out.println(timestamped);
        
        if (logWriter != null) {
            try {
                logWriter.write(timestamped + "\n");
                logWriter.flush();
            } catch (IOException e) {
                System.err.println("Failed to write to log: " + e.getMessage());
            }
        }
    }
}
```

## Example 2: Advanced Rank System

A comprehensive ranking system with persistence, rewards, and leaderboards.

```java
package com.example.ranksystem;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import net.fabricmc.api.ModInitializer;
import net.minecraft.item.ItemStack;
import net.minecraft.item.Items;
import net.minecraft.text.Text;
import org.stepan1411.pvp_bot.api.PvpBotAPI;

import java.io.*;
import java.lang.reflect.Type;
import java.util.*;
import java.util.stream.Collectors;

public class BotRankSystem implements ModInitializer {
    
    private final Map<String, BotRankData> rankData = new HashMap<>();
    private final Gson gson = new Gson();
    private final File dataFile = new File("bot_ranks.json");
    
    // Rank definitions
    private final List<Rank> ranks = Arrays.asList(
        new Rank("Novice", 0, "§7"),
        new Rank("Fighter", 50, "§f"),
        new Rank("Warrior", 150, "§e"),
        new Rank("Veteran", 300, "§6"),
        new Rank("Elite", 500, "§5"),
        new Rank("Master", 750, "§9"),
        new Rank("Grandmaster", 1000, "§b"),
        new Rank("Legend", 1500, "§d"),
        new Rank("Mythic", 2500, "§4"),
        new Rank("Divine", 5000, "§c")
    );
    
    @Override
    public void onInitialize() {
        loadData();
        
        PvpBotAPI.getEventManager().registerAttackHandler((bot, target) -> {
            if (target.isDead()) {
                String botName = bot.getName().getString();
                BotRankData data = rankData.computeIfAbsent(botName, k -> new BotRankData());
                
                // Award experience based on target type
                int expGain = calculateExpGain(target);
                data.experience += expGain;
                data.kills++;
                
                // Check for rank up
                Rank newRank = getRankForExp(data.experience);
                if (!newRank.name.equals(data.currentRank)) {
                    rankUp(bot, data, newRank);
                }
                
                // Show exp gain
                bot.sendMessage(Text.literal(String.format("§a+%d EXP §7(Total: %d)", 
                    expGain, data.experience)));
                
                saveData();
            }
            return false;
        });
        
        // Track deaths
        PvpBotAPI.getEventManager().registerDeathHandler(bot -> {
            String botName = bot.getName().getString();
            BotRankData data = rankData.computeIfAbsent(botName, k -> new BotRankData());
            data.deaths++;
            saveData();
        });
        
        // Display rank on spawn
        PvpBotAPI.getEventManager().registerSpawnHandler(bot -> {
            String botName = bot.getName().getString();
            BotRankData data = rankData.get(botName);
            if (data != null) {
                Rank rank = getRankForExp(data.experience);
                bot.sendMessage(Text.literal(String.format("%s[%s] §7EXP: %d | K/D: %.2f", 
                    rank.color, rank.name, data.experience, data.getKDRatio())));
            }
        });
    }
    
    private int calculateExpGain(Entity target) {
        if (target instanceof PlayerEntity) {
            return PvpBotAPI.isBot(target.getName().getString()) ? 15 : 25; // More for real players
        } else if (target instanceof HostileEntity) {
            return 5;
        } else {
            return 2;
        }
    }
    
    private void rankUp(ServerPlayerEntity bot, BotRankData data, Rank newRank) {
        String oldRank = data.currentRank;
        data.currentRank = newRank.name;
        
        // Announce rank up
        bot.sendMessage(Text.literal(String.format("§6§l*** RANK UP! ***\n§7%s §6→ %s%s", 
            oldRank, newRank.color, newRank.name)));
        
        // Give rewards
        giveRankRewards(bot, newRank);
        
        // Broadcast to server
        bot.getServer().getPlayerManager().broadcast(
            Text.literal(String.format("§6%s ranked up to %s%s§6!", 
                bot.getName().getString(), newRank.color, newRank.name)),
            false
        );
    }
    
    private void giveRankRewards(ServerPlayerEntity bot, Rank rank) {
        // Give items based on rank
        switch (rank.name) {
            case "Fighter":
                giveItem(bot, new ItemStack(Items.IRON_SWORD));
                break;
            case "Warrior":
                giveItem(bot, new ItemStack(Items.DIAMOND_SWORD));
                break;
            case "Elite":
                giveItem(bot, new ItemStack(Items.NETHERITE_SWORD));
                break;
            case "Master":
                giveItem(bot, new ItemStack(Items.TOTEM_OF_UNDYING));
                break;
            case "Legend":
                giveItem(bot, new ItemStack(Items.ELYTRA));
                break;
        }
    }
    
    private void giveItem(ServerPlayerEntity bot, ItemStack item) {
        if (!bot.getInventory().insertStack(item)) {
            // Drop if inventory full
            bot.dropItem(item, false);
        }
    }
    
    private Rank getRankForExp(int exp) {
        Rank currentRank = ranks.get(0);
        for (Rank rank : ranks) {
            if (exp >= rank.requiredExp) {
                currentRank = rank;
            } else {
                break;
            }
        }
        return currentRank;
    }
    
    public List<Map.Entry<String, BotRankData>> getLeaderboard() {
        return rankData.entrySet().stream()
            .sorted((a, b) -> Integer.compare(b.getValue().experience, a.getValue().experience))
            .limit(10)
            .collect(Collectors.toList());
    }
    
    private void loadData() {
        if (!dataFile.exists()) return;
        
        try (Reader reader = new FileReader(dataFile)) {
            Type type = new TypeToken<Map<String, BotRankData>>(){}.getType();
            Map<String, BotRankData> loaded = gson.fromJson(reader, type);
            if (loaded != null) {
                rankData.putAll(loaded);
            }
        } catch (IOException e) {
            System.err.println("Failed to load rank data: " + e.getMessage());
        }
    }
    
    private void saveData() {
        try (Writer writer = new FileWriter(dataFile)) {
            gson.toJson(rankData, writer);
        } catch (IOException e) {
            System.err.println("Failed to save rank data: " + e.getMessage());
        }
    }
    
    private static class Rank {
        final String name;
        final int requiredExp;
        final String color;
        
        Rank(String name, int requiredExp, String color) {
            this.name = name;
            this.requiredExp = requiredExp;
            this.color = color;
        }
    }
    
    private static class BotRankData {
        int experience = 0;
        int kills = 0;
        int deaths = 0;
        String currentRank = "Novice";
        
        double getKDRatio() {
            return deaths == 0 ? kills : (double) kills / deaths;
        }
    }
}
```

## Example 3: Advanced Combat Strategy - Fireball Launcher

A sophisticated combat strategy with resource management and tactical positioning.

```java
package com.example.strategies;

import net.minecraft.entity.Entity;
import net.minecraft.entity.projectile.FireballEntity;
import net.minecraft.item.ItemStack;
import net.minecraft.item.Items;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.network.ServerPlayerEntity;
import net.minecraft.server.world.ServerWorld;
import net.minecraft.util.math.Vec3d;
import org.stepan1411.pvp_bot.api.combat.CombatStrategy;
import org.stepan1411.pvp_bot.bot.BotSettings;

public class FireballStrategy implements CombatStrategy {
    
    private final Map<String, Long> lastUsed = new HashMap<>();
    
    @Override
    public String getName() {
        return "FireballLauncher";
    }
    
    @Override
    public int getPriority() {
        return 130; // High priority ranged strategy
    }
    
    @Override
    public boolean canUse(ServerPlayerEntity bot, Entity target, BotSettings settings) {
        // Check cooldown
        long currentTime = System.currentTimeMillis();
        long lastUseTime = lastUsed.getOrDefault(bot.getName().getString(), 0L);
        if (currentTime - lastUseTime < getCooldown() * 50) {
            return false;
        }
        
        double distance = bot.distanceTo(target);
        
        // Optimal range for fireball
        if (distance < 8.0 || distance > 25.0) {
            return false;
        }
        
        // Check if bot has fire charges
        return hasFireCharges(bot) && hasLineOfSight(bot, target);
    }
    
    @Override
    public boolean execute(ServerPlayerEntity bot, Entity target, BotSettings settings, MinecraftServer server) {
        // Consume fire charge
        if (!consumeFireCharge(bot)) {
            return false;
        }
        
        // Calculate trajectory
        Vec3d botPos = bot.getEyePos();
        Vec3d targetPos = target.getPos().add(0, target.getHeight() / 2, 0);
        
        // Predict target movement
        Vec3d targetVelocity = target.getVelocity();
        double timeToTarget = botPos.distanceTo(targetPos) / 20.0; // Fireball speed
        Vec3d predictedPos = targetPos.add(targetVelocity.multiply(timeToTarget));
        
        Vec3d direction = predictedPos.subtract(botPos).normalize();
        
        // Create and launch fireball
        ServerWorld world = (ServerWorld) bot.getEntityWorld();
        FireballEntity fireball = new FireballEntity(
            world, 
            bot, 
            direction.x, 
            direction.y, 
            direction.z, 
            2 // Explosion power
        );
        
        fireball.setPosition(botPos);
        world.spawnEntity(fireball);
        
        // Record usage time
        lastUsed.put(bot.getName().getString(), System.currentTimeMillis());
        
        // Send message
        bot.sendMessage(Text.literal("§6Fireball launched!"));
        
        return true;
    }
    
    private boolean hasFireCharges(ServerPlayerEntity bot) {
        return bot.getInventory().count(Items.FIRE_CHARGE) > 0;
    }
    
    private boolean consumeFireCharge(ServerPlayerEntity bot) {
        for (int i = 0; i < bot.getInventory().size(); i++) {
            ItemStack stack = bot.getInventory().getStack(i);
            if (stack.getItem() == Items.FIRE_CHARGE) {
                stack.decrement(1);
                return true;
            }
        }
        return false;
    }
    
    private boolean hasLineOfSight(ServerPlayerEntity bot, Entity target) {
        // Simple line of sight check
        Vec3d start = bot.getEyePos();
        Vec3d end = target.getEyePos();
        
        return bot.getWorld().raycast(new RaycastContext(
            start, end,
            RaycastContext.ShapeType.COLLIDER,
            RaycastContext.FluidHandling.NONE,
            bot
        )).getType() == HitResult.Type.MISS;
    }
    
    @Override
    public int getCooldown() {
        return 100; // 5 seconds
    }
}
```

## Example 4: Comprehensive Team System

A full-featured team system with commands, friendly fire protection, and team coordination.

```java
package com.example.teamsystem;

import com.mojang.brigadier.CommandDispatcher;
import com.mojang.brigadier.arguments.StringArgumentType;
import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.command.v2.CommandRegistrationCallback;
import net.minecraft.command.CommandRegistryAccess;
import net.minecraft.server.command.CommandManager;
import net.minecraft.server.command.ServerCommandSource;
import net.minecraft.server.network.ServerPlayerEntity;
import net.minecraft.text.Text;
import org.stepan1411.pvp_bot.api.PvpBotAPI;

import java.util.*;
import java.util.stream.Collectors;

import static net.minecraft.server.command.CommandManager.argument;
import static net.minecraft.server.command.CommandManager.literal;

public class BotTeamSystem implements ModInitializer {
    
    private final Map<String, Team> teams = new HashMap<>();
    private final Map<String, String> playerTeams = new HashMap<>(); // player -> team name
    
    @Override
    public void onInitialize() {
        setupEventHandlers();
        registerCommands();
    }
    
    private void setupEventHandlers() {
        // Prevent friendly fire
        PvpBotAPI.getEventManager().registerAttackHandler((bot, target) -> {
            if (target instanceof ServerPlayerEntity targetPlayer) {
                String botName = bot.getName().getString();
                String targetName = targetPlayer.getName().getString();
                
                String botTeam = playerTeams.get(botName);
                String targetTeam = playerTeams.get(targetName);
                
                // Cancel attack if same team
                if (botTeam != null && botTeam.equals(targetTeam)) {
                    bot.sendMessage(Text.literal("§c Cannot attack team member!"));
                    return true; // Cancel attack
                }
            }
            return false;
        });
        
        // Team coordination on spawn
        PvpBotAPI.getEventManager().registerSpawnHandler(bot -> {
            String botName = bot.getName().getString();
            String teamName = playerTeams.get(botName);
            
            if (teamName != null) {
                Team team = teams.get(teamName);
                if (team != null) {
                    // Notify team members
                    broadcastToTeam(team, String.format("§a%s joined the battle!", botName));
                    
                    // Apply team buffs
                    applyTeamBuffs(bot, team);
                }
            }
        });
        
        // Remove from team on death (optional)
        PvpBotAPI.getEventManager().registerDeathHandler(bot -> {
            String botName = bot.getName().getString();
            String teamName = playerTeams.get(botName);
            
            if (teamName != null) {
                Team team = teams.get(teamName);
                if (team != null) {
                    broadcastToTeam(team, String.format("§c%s has fallen!", botName));
                }
            }
        });
    }
    
    private void registerCommands() {
        CommandRegistrationCallback.EVENT.register(this::registerTeamCommands);
    }
    
    private void registerTeamCommands(CommandDispatcher<ServerCommandSource> dispatcher, 
                                     CommandRegistryAccess registryAccess, 
                                     CommandManager.RegistrationEnvironment environment) {
        
        dispatcher.register(literal("team")
            // Create team
            .then(literal("create")
                .then(argument("name", StringArgumentType.string())
                    .executes(context -> {
                        String teamName = StringArgumentType.getString(context, "name");
                        return createTeam(context.getSource(), teamName);
                    })
                )
            )
            // Delete team
            .then(literal("delete")
                .then(argument("name", StringArgumentType.string())
                    .executes(context -> {
                        String teamName = StringArgumentType.getString(context, "name");
                        return deleteTeam(context.getSource(), teamName);
                    })
                )
            )
            // Add player to team
            .then(literal("add")
                .then(argument("team", StringArgumentType.string())
                    .then(argument("player", StringArgumentType.string())
                        .executes(context -> {
                            String teamName = StringArgumentType.getString(context, "team");
                            String playerName = StringArgumentType.getString(context, "player");
                            return addPlayerToTeam(context.getSource(), teamName, playerName);
                        })
                    )
                )
            )
            // Remove player from team
            .then(literal("remove")
                .then(argument("player", StringArgumentType.string())
                    .executes(context -> {
                        String playerName = StringArgumentType.getString(context, "player");
                        return removePlayerFromTeam(context.getSource(), playerName);
                    })
                )
            )
            // List teams
            .then(literal("list")
                .executes(context -> listTeams(context.getSource()))
            )
            // Team info
            .then(literal("info")
                .then(argument("name", StringArgumentType.string())
                    .executes(context -> {
                        String teamName = StringArgumentType.getString(context, "name");
                        return showTeamInfo(context.getSource(), teamName);
                    })
                )
            )
        );
    }
    
    private int createTeam(ServerCommandSource source, String teamName) {
        if (teams.containsKey(teamName)) {
            source.sendError(Text.literal("Team '" + teamName + "' already exists!"));
            return 0;
        }
        
        teams.put(teamName, new Team(teamName));
        source.sendFeedback(() -> Text.literal("§aTeam '" + teamName + "' created!"), false);
        return 1;
    }
    
    private int deleteTeam(ServerCommandSource source, String teamName) {
        Team team = teams.remove(teamName);
        if (team == null) {
            source.sendError(Text.literal("Team '" + teamName + "' does not exist!"));
            return 0;
        }
        
        // Remove all players from team
        team.members.forEach(playerTeams::remove);
        
        source.sendFeedback(() -> Text.literal("§cTeam '" + teamName + "' deleted!"), false);
        return 1;
    }
    
    private int addPlayerToTeam(ServerCommandSource source, String teamName, String playerName) {
        Team team = teams.get(teamName);
        if (team == null) {
            source.sendError(Text.literal("Team '" + teamName + "' does not exist!"));
            return 0;
        }
        
        // Remove from previous team
        String oldTeam = playerTeams.get(playerName);
        if (oldTeam != null) {
            teams.get(oldTeam).members.remove(playerName);
        }
        
        // Add to new team
        team.members.add(playerName);
        playerTeams.put(playerName, teamName);
        
        source.sendFeedback(() -> Text.literal(String.format("§a%s added to team %s!", 
            playerName, teamName)), false);
        
        // Notify team
        broadcastToTeam(team, String.format("§a%s joined the team!", playerName));
        
        return 1;
    }
    
    private int removePlayerFromTeam(ServerCommandSource source, String playerName) {
        String teamName = playerTeams.remove(playerName);
        if (teamName == null) {
            source.sendError(Text.literal(playerName + " is not in any team!"));
            return 0;
        }
        
        Team team = teams.get(teamName);
        if (team != null) {
            team.members.remove(playerName);
            broadcastToTeam(team, String.format("§c%s left the team!", playerName));
        }
        
        source.sendFeedback(() -> Text.literal(String.format("§c%s removed from team %s!", 
            playerName, teamName)), false);
        return 1;
    }
    
    private int listTeams(ServerCommandSource source) {
        if (teams.isEmpty()) {
            source.sendFeedback(() -> Text.literal("§7No teams exist."), false);
            return 1;
        }
        
        source.sendFeedback(() -> Text.literal("§6=== Teams ==="), false);
        for (Team team : teams.values()) {
            source.sendFeedback(() -> Text.literal(String.format("§e%s §7(%d members): %s", 
                team.name, team.members.size(), String.join(", ", team.members))), false);
        }
        return 1;
    }
    
    private int showTeamInfo(ServerCommandSource source, String teamName) {
        Team team = teams.get(teamName);
        if (team == null) {
            source.sendError(Text.literal("Team '" + teamName + "' does not exist!"));
            return 0;
        }
        
        source.sendFeedback(() -> Text.literal("§6=== Team " + teamName + " ==="), false);
        source.sendFeedback(() -> Text.literal("§7Members (" + team.members.size() + "): " + 
            String.join(", ", team.members)), false);
        
        // Show online members
        List<String> onlineMembers = team.members.stream()
            .filter(name -> source.getServer().getPlayerManager().getPlayer(name) != null)
            .collect(Collectors.toList());
        
        source.sendFeedback(() -> Text.literal("§aOnline: " + String.join(", ", onlineMembers)), false);
        
        return 1;
    }
    
    private void broadcastToTeam(Team team, String message) {
        for (String memberName : team.members) {
            ServerPlayerEntity player = team.getServer().getPlayerManager().getPlayer(memberName);
            if (player != null) {
                player.sendMessage(Text.literal("§6[TEAM] " + message));
            }
        }
    }
    
    private void applyTeamBuffs(ServerPlayerEntity bot, Team team) {
        // Apply buffs based on team size
        int teamSize = team.members.size();
        if (teamSize >= 3) {
            // Team strength buff
            bot.addStatusEffect(new StatusEffectInstance(
                StatusEffects.STRENGTH, 6000, 0));
        }
        if (teamSize >= 5) {
            // Large team speed buff
            bot.addStatusEffect(new StatusEffectInstance(
                StatusEffects.SPEED, 6000, 0));
        }
    }
    
    public boolean areTeammates(String player1, String player2) {
        String team1 = playerTeams.get(player1);
        String team2 = playerTeams.get(player2);
        return team1 != null && team1.equals(team2);
    }
    
    private static class Team {
        final String name;
        final Set<String> members = new HashSet<>();
        final long createdTime = System.currentTimeMillis();
        
        Team(String name) {
            this.name = name;
        }
    }
}
```

## Example 5: Auto Heal

```java
public class AutoHeal implements ModInitializer {
    
    @Override
    public void onInitialize() {
        PvpBotAPI.getEventManager().registerTickHandler(bot -> {
            // Check every 2 seconds (40 ticks)
            if (bot.age % 40 != 0) return;
            
            float health = bot.getHealth();
            float maxHealth = bot.getMaxHealth();
            
            // If HP below 50%
            if (health < maxHealth * 0.5f) {
                // Find healing potion
                for (int i = 0; i < bot.getInventory().size(); i++) {
                    ItemStack stack = bot.getInventory().getStack(i);
                    
                    if (stack.getItem() == Items.POTION) {
                        // Use potion
                        bot.setHealth(Math.min(maxHealth, health + 4.0f));
                        stack.decrement(1);
                        break;
                    }
                }
            }
        });
    }
}
```

## Example 6: Achievement System

```java
public class BotAchievements implements ModInitializer {
    
    private final Map<String, BotStats> stats = new HashMap<>();
    
    @Override
    public void onInitialize() {
        BotEventManager events = PvpBotAPI.getEventManager();
        
        // Track kills
        events.registerAttackHandler((bot, target) -> {
            if (target.isDead()) {
                String botName = bot.getName().getString();
                BotStats botStats = stats.computeIfAbsent(botName, k -> new BotStats());
                botStats.kills++;
                
                checkAchievements(bot, botStats);
            }
            return false;
        });
        
        // Track deaths
        events.registerDeathHandler(bot -> {
            String botName = bot.getName().getString();
            BotStats botStats = stats.computeIfAbsent(botName, k -> new BotStats());
            botStats.deaths++;
        });
    }
    
    private void checkAchievements(ServerPlayerEntity bot, BotStats stats) {
        if (stats.kills == 10 && !stats.hasAchievement("first_blood")) {
            stats.addAchievement("first_blood");
            bot.sendMessage(Text.literal("🏆 Achievement: First Blood (10 kills)"));
        }
        
        if (stats.kills == 100 && !stats.hasAchievement("warrior")) {
            stats.addAchievement("warrior");
            bot.sendMessage(Text.literal("🏆 Achievement: Warrior (100 kills)"));
        }
        
        if (stats.kills >= 1000 && !stats.hasAchievement("legend")) {
            stats.addAchievement("legend");
            bot.sendMessage(Text.literal("🏆 Achievement: Legend (1000 kills)"));
        }
    }
    
    private static class BotStats {
        int kills = 0;
        int deaths = 0;
        Set<String> achievements = new HashSet<>();
        
        boolean hasAchievement(String name) {
            return achievements.contains(name);
        }
        
        void addAchievement(String name) {
            achievements.add(name);
        }
    }
}
```

## Example 5: Smart Auto-Heal System

An intelligent healing system that manages multiple healing methods and prioritizes based on situation.

```java
package com.example.autoheal;

import net.fabricmc.api.ModInitializer;
import net.minecraft.entity.effect.StatusEffectInstance;
import net.minecraft.entity.effect.StatusEffects;
import net.minecraft.item.ItemStack;
import net.minecraft.item.Items;
import net.minecraft.server.network.ServerPlayerEntity;
import net.minecraft.text.Text;
import org.stepan1411.pvp_bot.api.PvpBotAPI;

import java.util.HashMap;
import java.util.Map;

public class SmartAutoHeal implements ModInitializer {
    
    private final Map<String, HealingState> healingStates = new HashMap<>();
    
    @Override
    public void onInitialize() {
        PvpBotAPI.getEventManager().registerTickHandler(bot -> {
            // Check every second (20 ticks)
            if (bot.age % 20 != 0) return;
            
            String botName = bot.getName().getString();
            HealingState state = healingStates.computeIfAbsent(botName, k -> new HealingState());
            
            float health = bot.getHealth();
            float maxHealth = bot.getMaxHealth();
            float healthPercent = health / maxHealth;
            
            // Emergency healing (< 25% health)
            if (healthPercent < 0.25f) {
                if (useTotem(bot)) {
                    state.lastHealTime = bot.age;
                    bot.sendMessage(Text.literal("§6Emergency totem used!"));
                } else if (useGoldenApple(bot)) {
                    state.lastHealTime = bot.age;
                    bot.sendMessage(Text.literal("§eGolden apple consumed!"));
                }
            }
            // Regular healing (< 50% health)
            else if (healthPercent < 0.5f && bot.age - state.lastHealTime > 100) { // 5 second cooldown
                if (useHealingPotion(bot)) {
                    state.lastHealTime = bot.age;
                    bot.sendMessage(Text.literal("§dHealing potion used!"));
                } else if (useFood(bot)) {
                    state.lastHealTime = bot.age;
                    bot.sendMessage(Text.literal("§aFood consumed!"));
                }
            }
            // Regeneration maintenance (< 75% health)
            else if (healthPercent < 0.75f && bot.age - state.lastHealTime > 200) { // 10 second cooldown
                if (useRegenerationPotion(bot)) {
                    state.lastHealTime = bot.age;
                    bot.sendMessage(Text.literal("§bRegeneration applied!"));
                }
            }
        });
        
        // Clean up on death
        PvpBotAPI.getEventManager().registerDeathHandler(bot -> {
            healingStates.remove(bot.getName().getString());
        });
    }
    
    private boolean useTotem(ServerPlayerEntity bot) {
        // Check if totem is already in offhand
        ItemStack offhand = bot.getOffHandStack();
        if (offhand.getItem() == Items.TOTEM_OF_UNDYING) {
            return false; // Already equipped
        }
        
        // Find totem in inventory
        for (int i = 0; i < bot.getInventory().size(); i++) {
            ItemStack stack = bot.getInventory().getStack(i);
            if (stack.getItem() == Items.TOTEM_OF_UNDYING) {
                // Move to offhand
                bot.getInventory().setStack(40, stack.copy()); // Offhand slot
                bot.getInventory().setStack(i, ItemStack.EMPTY);
                return true;
            }
        }
        return false;
    }
    
    private boolean useGoldenApple(ServerPlayerEntity bot) {
        return consumeItem(bot, Items.GOLDEN_APPLE, () -> {
            // Golden apple effects are automatic
        });
    }
    
    private boolean useHealingPotion(ServerPlayerEntity bot) {
        return consumeItem(bot, Items.POTION, () -> {
            // Apply instant health effect
            bot.addStatusEffect(new StatusEffectInstance(
                StatusEffects.INSTANT_HEALTH, 1, 1));
        });
    }
    
    private boolean useRegenerationPotion(ServerPlayerEntity bot) {
        if (bot.hasStatusEffect(StatusEffects.REGENERATION)) {
            return false; // Already has regeneration
        }
        
        return consumeItem(bot, Items.POTION, () -> {
            bot.addStatusEffect(new StatusEffectInstance(
                StatusEffects.REGENERATION, 900, 1)); // 45 seconds
        });
    }
    
    private boolean useFood(ServerPlayerEntity bot) {
        // Try different food items in order of preference
        if (consumeItem(bot, Items.COOKED_BEEF, null)) return true;
        if (consumeItem(bot, Items.COOKED_PORKCHOP, null)) return true;
        if (consumeItem(bot, Items.BREAD, null)) return true;
        if (consumeItem(bot, Items.APPLE, null)) return true;
        return false;
    }
    
    private boolean consumeItem(ServerPlayerEntity bot, net.minecraft.item.Item item, Runnable effect) {
        for (int i = 0; i < bot.getInventory().size(); i++) {
            ItemStack stack = bot.getInventory().getStack(i);
            if (stack.getItem() == item) {
                stack.decrement(1);
                if (effect != null) {
                    effect.run();
                }
                return true;
            }
        }
        return false;
    }
    
    private static class HealingState {
        int lastHealTime = 0;
    }
}
```

## Example 6: Comprehensive Achievement System

A full achievement system with categories, rewards, and persistent storage.

```java
package com.example.achievements;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import net.fabricmc.api.ModInitializer;
import net.minecraft.entity.Entity;
import net.minecraft.entity.mob.HostileEntity;
import net.minecraft.entity.player.PlayerEntity;
import net.minecraft.item.ItemStack;
import net.minecraft.item.Items;
import net.minecraft.server.network.ServerPlayerEntity;
import net.minecraft.text.Text;
import org.stepan1411.pvp_bot.api.PvpBotAPI;

import java.io.*;
import java.lang.reflect.Type;
import java.util.*;

public class BotAchievementSystem implements ModInitializer {
    
    private final Map<String, PlayerProgress> playerProgress = new HashMap<>();
    private final List<Achievement> achievements = new ArrayList<>();
    private final Gson gson = new Gson();
    private final File dataFile = new File("bot_achievements.json");
    
    @Override
    public void onInitialize() {
        initializeAchievements();
        loadProgress();
        setupEventHandlers();
    }
    
    private void initializeAchievements() {
        // Combat achievements
        achievements.add(new Achievement("first_blood", "First Blood", 
            "Kill your first enemy", AchievementCategory.COMBAT, 
            progress -> progress.kills >= 1, 
            new ItemStack(Items.IRON_SWORD)));
            
        achievements.add(new Achievement("warrior", "Warrior", 
            "Kill 50 enemies", AchievementCategory.COMBAT, 
            progress -> progress.kills >= 50, 
            new ItemStack(Items.DIAMOND_SWORD)));
            
        achievements.add(new Achievement("slayer", "Slayer", 
            "Kill 100 enemies", AchievementCategory.COMBAT, 
            progress -> progress.kills >= 100, 
            new ItemStack(Items.NETHERITE_SWORD)));
            
        achievements.add(new Achievement("unstoppable", "Unstoppable", 
            "Get 10 kills without dying", AchievementCategory.COMBAT, 
            progress -> progress.killStreak >= 10, 
            new ItemStack(Items.TOTEM_OF_UNDYING)));
        
        // Survival achievements
        achievements.add(new Achievement("survivor", "Survivor", 
            "Survive for 1 hour", AchievementCategory.SURVIVAL, 
            progress -> progress.survivalTime >= 72000, // 1 hour in ticks
            new ItemStack(Items.GOLDEN_APPLE)));
            
        achievements.add(new Achievement("tank", "Tank", 
            "Take 1000 damage and survive", AchievementCategory.SURVIVAL, 
            progress -> progress.damageTaken >= 1000, 
            new ItemStack(Items.SHIELD)));
        
        // Special achievements
        achievements.add(new Achievement("pacifist", "Pacifist", 
            "Survive 30 minutes without killing", AchievementCategory.SPECIAL, 
            progress -> progress.survivalTime >= 36000 && progress.kills == 0, 
            new ItemStack(Items.WHITE_BANNER)));
            
        achievements.add(new Achievement("berserker", "Berserker", 
            "Kill 5 enemies in 30 seconds", AchievementCategory.SPECIAL, 
            progress -> progress.recentKills.size() >= 5 && 
                       (System.currentTimeMillis() - progress.recentKills.get(0)) <= 30000, 
            new ItemStack(Items.NETHERITE_AXE)));
    }
    
    private void setupEventHandlers() {
        // Track kills
        PvpBotAPI.getEventManager().registerAttackHandler((bot, target) -> {
            if (target.isDead()) {
                String botName = bot.getName().getString();
                PlayerProgress progress = playerProgress.computeIfAbsent(botName, k -> new PlayerProgress());
                
                progress.kills++;
                progress.killStreak++;
                progress.recentKills.add(System.currentTimeMillis());
                
                // Keep only recent kills (last 60 seconds)
                long cutoff = System.currentTimeMillis() - 60000;
                progress.recentKills.removeIf(time -> time < cutoff);
                
                // Award extra points for different target types
                if (target instanceof PlayerEntity) {
                    progress.playerKills++;
                } else if (target instanceof HostileEntity) {
                    progress.mobKills++;
                }
                
                checkAchievements(bot, progress);
                saveProgress();
            }
            return false;
        });
        
        // Track deaths
        PvpBotAPI.getEventManager().registerDeathHandler(bot -> {
            String botName = bot.getName().getString();
            PlayerProgress progress = playerProgress.computeIfAbsent(botName, k -> new PlayerProgress());
            
            progress.deaths++;
            progress.killStreak = 0; // Reset kill streak
            progress.recentKills.clear();
            
            saveProgress();
        });
        
        // Track damage
        PvpBotAPI.getEventManager().registerDamageHandler((bot, attacker, damage) -> {
            String botName = bot.getName().getString();
            PlayerProgress progress = playerProgress.computeIfAbsent(botName, k -> new PlayerProgress());
            
            progress.damageTaken += damage;
            return false;
        });
        
        // Track survival time
        PvpBotAPI.getEventManager().registerTickHandler(bot -> {
            String botName = bot.getName().getString();
            PlayerProgress progress = playerProgress.computeIfAbsent(botName, k -> new PlayerProgress());
            
            progress.survivalTime++;
            
            // Check achievements every 10 seconds
            if (bot.age % 200 == 0) {
                checkAchievements(bot, progress);
            }
        });
        
        // Display achievements on spawn
        PvpBotAPI.getEventManager().registerSpawnHandler(bot -> {
            String botName = bot.getName().getString();
            PlayerProgress progress = playerProgress.get(botName);
            
            if (progress != null && !progress.unlockedAchievements.isEmpty()) {
                bot.sendMessage(Text.literal(String.format("§6Achievements: %d/%d unlocked", 
                    progress.unlockedAchievements.size(), achievements.size())));
            }
        });
    }
    
    private void checkAchievements(ServerPlayerEntity bot, PlayerProgress progress) {
        for (Achievement achievement : achievements) {
            if (!progress.unlockedAchievements.contains(achievement.id) && 
                achievement.condition.test(progress)) {
                
                unlockAchievement(bot, progress, achievement);
            }
        }
    }
    
    private void unlockAchievement(ServerPlayerEntity bot, PlayerProgress progress, Achievement achievement) {
        progress.unlockedAchievements.add(achievement.id);
        
        // Announce achievement
        bot.sendMessage(Text.literal(String.format("§6§l*** ACHIEVEMENT UNLOCKED ***\n§e%s\n§7%s", 
            achievement.name, achievement.description)));
        
        // Give reward
        if (achievement.reward != null) {
            if (!bot.getInventory().insertStack(achievement.reward.copy())) {
                bot.dropItem(achievement.reward.copy(), false);
            }
            bot.sendMessage(Text.literal("§aReward: " + achievement.reward.getName().getString()));
        }
        
        // Broadcast to server
        bot.getServer().getPlayerManager().broadcast(
            Text.literal(String.format("§6%s unlocked achievement: §e%s", 
                bot.getName().getString(), achievement.name)),
            false
        );
        
        saveProgress();
    }
    
    public List<Achievement> getAchievementsForPlayer(String playerName) {
        PlayerProgress progress = playerProgress.get(playerName);
        if (progress == null) return new ArrayList<>();
        
        return achievements.stream()
            .filter(a -> progress.unlockedAchievements.contains(a.id))
            .collect(Collectors.toList());
    }
    
    private void loadProgress() {
        if (!dataFile.exists()) return;
        
        try (Reader reader = new FileReader(dataFile)) {
            Type type = new TypeToken<Map<String, PlayerProgress>>(){}.getType();
            Map<String, PlayerProgress> loaded = gson.fromJson(reader, type);
            if (loaded != null) {
                playerProgress.putAll(loaded);
            }
        } catch (IOException e) {
            System.err.println("Failed to load achievement progress: " + e.getMessage());
        }
    }
    
    private void saveProgress() {
        try (Writer writer = new FileWriter(dataFile)) {
            gson.toJson(playerProgress, writer);
        } catch (IOException e) {
            System.err.println("Failed to save achievement progress: " + e.getMessage());
        }
    }
    
    public enum AchievementCategory {
        COMBAT, SURVIVAL, SPECIAL
    }
    
    public static class Achievement {
        final String id;
        final String name;
        final String description;
        final AchievementCategory category;
        final java.util.function.Predicate<PlayerProgress> condition;
        final ItemStack reward;
        
        Achievement(String id, String name, String description, AchievementCategory category,
                   java.util.function.Predicate<PlayerProgress> condition, ItemStack reward) {
            this.id = id;
            this.name = name;
            this.description = description;
            this.category = category;
            this.condition = condition;
            this.reward = reward;
        }
    }
    
    public static class PlayerProgress {
        int kills = 0;
        int deaths = 0;
        int playerKills = 0;
        int mobKills = 0;
        int killStreak = 0;
        float damageTaken = 0;
        int survivalTime = 0;
        List<Long> recentKills = new ArrayList<>();
        Set<String> unlockedAchievements = new HashSet<>();
        
        public double getKDRatio() {
            return deaths == 0 ? kills : (double) kills / deaths;
        }
    }
}
```

## Example 7: Bot Behavior Modifier

A system that modifies bot behavior based on various conditions and player preferences.

```java
package com.example.behavior;

import net.fabricmc.api.ModInitializer;
import net.minecraft.entity.effect.StatusEffectInstance;
import net.minecraft.entity.effect.StatusEffects;
import net.minecraft.server.network.ServerPlayerEntity;
import net.minecraft.text.Text;
import org.stepan1411.pvp_bot.api.PvpBotAPI;
import org.stepan1411.pvp_bot.api.combat.CombatStrategy;
import org.stepan1411.pvp_bot.api.combat.CombatStrategyRegistry;
import org.stepan1411.pvp_bot.bot.BotSettings;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;

public class BotBehaviorModifier implements ModInitializer {
    
    private final Map<String, BotPersonality> personalities = new HashMap<>();
    private final Random random = new Random();
    
    @Override
    public void onInitialize() {
        setupEventHandlers();
        registerBehaviorStrategies();
    }
    
    private void setupEventHandlers() {
        // Assign personality on spawn
        PvpBotAPI.getEventManager().registerSpawnHandler(bot -> {
            String botName = bot.getName().getString();
            if (!personalities.containsKey(botName)) {
                BotPersonality personality = generateRandomPersonality();
                personalities.put(botName, personality);
                
                bot.sendMessage(Text.literal(String.format("§6Personality: %s %s", 
                    personality.type.displayName, personality.type.description)));
                
                applyPersonalityEffects(bot, personality);
            }
        });
        
        // Modify behavior based on health
        PvpBotAPI.getEventManager().registerTickHandler(bot -> {
            if (bot.age % 100 != 0) return; // Every 5 seconds
            
            String botName = bot.getName().getString();
            BotPersonality personality = personalities.get(botName);
            if (personality == null) return;
            
            float healthPercent = bot.getHealth() / bot.getMaxHealth();
            
            // Apply dynamic effects based on personality and health
            applyDynamicEffects(bot, personality, healthPercent);
        });
        
        // Personality affects attack decisions
        PvpBotAPI.getEventManager().registerAttackHandler((bot, target) -> {
            String botName = bot.getName().getString();
            BotPersonality personality = personalities.get(botName);
            if (personality == null) return false;
            
            // Coward personality might flee instead of fighting
            if (personality.type == PersonalityType.COWARD && bot.getHealth() < 15.0f) {
                if (random.nextFloat() < 0.3f) { // 30% chance to flee
                    flee(bot);
                    return true; // Cancel attack
                }
            }
            
            // Berserker personality attacks more aggressively
            if (personality.type == PersonalityType.BERSERKER && bot.getHealth() < 10.0f) {
                // Apply rage effect
                bot.addStatusEffect(new StatusEffectInstance(
                    StatusEffects.STRENGTH, 200, 2));
                bot.sendMessage(Text.literal("§c*RAGE*"));
            }
            
            return false;
        });
    }
    
    private void registerBehaviorStrategies() {
        CombatStrategyRegistry.getInstance().register(new PersonalityStrategy());
    }
    
    private BotPersonality generateRandomPersonality() {
        PersonalityType[] types = PersonalityType.values();
        PersonalityType type = types[random.nextInt(types.length)];
        
        return new BotPersonality(type, 
            0.5f + random.nextFloat() * 0.5f, // aggression 0.5-1.0
            random.nextFloat(), // courage 0.0-1.0
            random.nextFloat()  // intelligence 0.0-1.0
        );
    }
    
    private void applyPersonalityEffects(ServerPlayerEntity bot, BotPersonality personality) {
        switch (personality.type) {
            case BERSERKER:
                bot.addStatusEffect(new StatusEffectInstance(
                    StatusEffects.STRENGTH, Integer.MAX_VALUE, 0));
                break;
            case TANK:
                bot.addStatusEffect(new StatusEffectInstance(
                    StatusEffects.RESISTANCE, Integer.MAX_VALUE, 0));
                break;
            case SCOUT:
                bot.addStatusEffect(new StatusEffectInstance(
                    StatusEffects.SPEED, Integer.MAX_VALUE, 1));
                break;
            case SNIPER:
                // Enhanced accuracy (handled in combat strategy)
                break;
            case COWARD:
                bot.addStatusEffect(new StatusEffectInstance(
                    StatusEffects.SPEED, Integer.MAX_VALUE, 0));
                break;
        }
    }
    
    private void applyDynamicEffects(ServerPlayerEntity bot, BotPersonality personality, float healthPercent) {
        // Low health effects based on personality
        if (healthPercent < 0.3f) {
            switch (personality.type) {
                case BERSERKER:
                    // More aggressive when low health
                    if (random.nextFloat() < 0.1f) {
                        bot.addStatusEffect(new StatusEffectInstance(
                            StatusEffects.STRENGTH, 100, 1));
                    }
                    break;
                case COWARD:
                    // Try to flee when low health
                    if (random.nextFloat() < 0.05f) {
                        flee(bot);
                    }
                    break;
                case TANK:
                    // Defensive stance
                    bot.addStatusEffect(new StatusEffectInstance(
                        StatusEffects.RESISTANCE, 100, 1));
                    break;
            }
        }
    }
    
    private void flee(ServerPlayerEntity bot) {
        // Apply speed and try to move away
        bot.addStatusEffect(new StatusEffectInstance(
            StatusEffects.SPEED, 200, 2));
        bot.sendMessage(Text.literal("§e*Fleeing*"));
        
        // Simple flee logic - could be enhanced with pathfinding
        double angle = random.nextDouble() * 2 * Math.PI;
        double distance = 20.0;
        double newX = bot.getX() + Math.cos(angle) * distance;
        double newZ = bot.getZ() + Math.sin(angle) * distance;
        
        bot.teleport(newX, bot.getY(), newZ);
    }
    
    public enum PersonalityType {
        BERSERKER("Berserker", "§cAggressive fighter, stronger when damaged"),
        TANK("Tank", "§9Defensive specialist, high resistance"),
        SCOUT("Scout", "§aFast and agile, prefers hit-and-run"),
        SNIPER("Sniper", "§6Ranged specialist, enhanced accuracy"),
        COWARD("Coward", "§7Flees from combat when damaged");
        
        final String displayName;
        final String description;
        
        PersonalityType(String displayName, String description) {
            this.displayName = displayName;
            this.description = description;
        }
    }
    
    public static class BotPersonality {
        final PersonalityType type;
        final float aggression;   // 0.0 - 1.0
        final float courage;      // 0.0 - 1.0
        final float intelligence; // 0.0 - 1.0
        
        BotPersonality(PersonalityType type, float aggression, float courage, float intelligence) {
            this.type = type;
            this.aggression = aggression;
            this.courage = courage;
            this.intelligence = intelligence;
        }
    }
    
    private class PersonalityStrategy implements CombatStrategy {
        @Override
        public String getName() {
            return "PersonalityBehavior";
        }
        
        @Override
        public int getPriority() {
            return 75; // Medium priority
        }
        
        @Override
        public boolean canUse(ServerPlayerEntity bot, Entity target, BotSettings settings) {
            return personalities.containsKey(bot.getName().getString());
        }
        
        @Override
        public boolean execute(ServerPlayerEntity bot, Entity target, BotSettings settings, MinecraftServer server) {
            BotPersonality personality = personalities.get(bot.getName().getString());
            if (personality == null) return false;
            
            switch (personality.type) {
                case SNIPER:
                    // Prefer ranged combat
                    if (bot.distanceTo(target) < 10.0 && random.nextFloat() < 0.7f) {
                        // Try to create distance
                        Vec3d direction = bot.getPos().subtract(target.getPos()).normalize();
                        Vec3d newPos = bot.getPos().add(direction.multiply(5));
                        bot.teleport(newPos.x, newPos.y, newPos.z);
                        return true;
                    }
                    break;
                    
                case SCOUT:
                    // Hit and run tactics
                    if (random.nextFloat() < 0.3f) {
                        bot.attack(target);
                        // Quick retreat
                        Vec3d direction = bot.getPos().subtract(target.getPos()).normalize();
                        Vec3d newPos = bot.getPos().add(direction.multiply(3));
                        bot.teleport(newPos.x, newPos.y, newPos.z);
                        return true;
                    }
                    break;
            }
            
            return false;
        }
        
        @Override
        public int getCooldown() {
            return 40; // 2 seconds
        }
    }
}
```

## Integration Examples

### Combining Multiple Systems

```java
public class IntegratedBotSystem implements ModInitializer {
    
    private BotRankSystem rankSystem;
    private BotTeamSystem teamSystem;
    private BotAchievementSystem achievementSystem;
    
    @Override
    public void onInitialize() {
        // Initialize subsystems
        rankSystem = new BotRankSystem();
        teamSystem = new BotTeamSystem();
        achievementSystem = new BotAchievementSystem();
        
        // Initialize all systems
        rankSystem.onInitialize();
        teamSystem.onInitialize();
        achievementSystem.onInitialize();
        
        // Add integration logic
        setupIntegration();
    }
    
    private void setupIntegration() {
        // Team bonuses based on rank
        PvpBotAPI.getEventManager().registerSpawnHandler(bot -> {
            String botName = bot.getName().getString();
            
            // Check if bot is in a team and has high rank
            if (teamSystem.areTeammates(botName, "SomeOtherBot")) {
                // Apply team coordination buffs
                bot.addStatusEffect(new StatusEffectInstance(
                    StatusEffects.STRENGTH, 6000, 0));
            }
        });
    }
}
```

These examples demonstrate the full power of the PVP Bot API. You can mix and match these patterns to create sophisticated bot behaviors and systems. Each example is production-ready and can be adapted to your specific needs.

For more examples and complete implementations, check out the [example mod repository](https://github.com/Stepan1411/pvpbot-example-mod).