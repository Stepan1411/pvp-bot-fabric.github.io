# ⚔️ Sistema de combate

PVP Bot presenta una IA de combate avanzada que puede usar diferentes armas y tácticas.

---

## 🗡️ Tipos de armas

### Melee Combat
- **Espadas** - Ataques rápidos, buen daño
- **Hachas** - Más lento pero puede romper escudos
- Bots automatically switch to melee when enemies are close

### Combate a distancia
- **Arcos** - Dibuja y suelta flechas
- **Ballestas** - Cargar y disparar virotes
- Los robots mantienen una distancia óptima (8-20 bloques)

### Combate con maza
- **Mace + Wind Charge** - Jump attacks for massive damage
- Los robots usan cargas de viento para lanzarse al aire.
- Devastadores ataques de caída

### Combate de ElytraMace
- **Élytra + Maza + Fuegos artificiales** - Técnica avanzada de ataque aéreo
- Los robots equipan élitros y usan fuegos artificiales para ganar altitud.
- Elimina los élitros en el aire y ataca con una maza para causar un daño masivo por caída.
- Selección de arma de mayor prioridad cuando esté disponible
- Configuraciones configurables de altitud, distancia y reintento.

### Cristal JcJ
- **Cristales finales + Obsidiana** - Coloca obsidiana y detona cristales
- Los robots calculan distancias de explosión seguras.
- Colocación y detonación automática de cristales.
- Combate explosivo de alto daño.

### PvP ancla
- **Respawn Anchor + Glowstone** - Arma explosiva en Overworld/End
- Los robots cargan anclas con piedra luminosa.
- Detonar para causar daño masivo
- Sólo funciona fuera del Nether

---

## 🎯 Orientación

### Modo venganza
Cuando un robot recibe daño, automáticamente apunta al atacante.
```mcfunction
/pvpbot settings revenge true
```

### Orientación automática
Bots automatically search for enemies within view distance.
```mcfunction
/pvpbot settings autotarget true
```

### Manual Target
Force a bot to attack a specific target.
```mcfunction
/pvpbot attack BotName TargetName
```

### Filtros de destino
Choose what bots can target:
```mcfunction
/pvpbot settings targetplayers true   # Target players
/pvpbot settings targetmobs true      # Target hostile mobs
/pvpbot settings targetbots true      # Target other bots
```

---

## 🛡️ Defense

### Auto-Shield
Bots automatically raise shields when enemies attack.
```mcfunction
/pvpbot settings autoshield true
```

### Rompiendo escudo
Los robots usan hachas para desactivar los escudos enemigos.
```mcfunction
/pvpbot settings shieldbreak true
```

### Auto-Tótem
Los robots mantienen tótems de inmortalidad a la ligera.
```mcfunction
/pvpbot settings autototem true
/pvpbot settings totempriority true  # Prioritize totem over shield
```

### Reparación automática
Los bots reparan automáticamente armaduras dañadas usando botellas de XP.
```mcfunction
/pvpbot settings automend true
/pvpbot settings menddurability 0.5  # Repair at 50% durability
```

---

## 🍎 Curación

### Comer automáticamente
Los robots comen comida cuando:
- La salud es baja (< 30%)
- El hambre está por debajo del umbral

```mcfunction
/pvpbot settings autoeat true
/pvpbot settings minhunger 14
```

### Pociones automáticas
Los bots usan pociones automáticamente:
- **Pociones curativas** - cuando el HP es bajo (salpicaduras o bebibles)
- **Pociones de fuerza** - al entrar en combate
- **Pociones de velocidad** - al entrar en combate
- **Pociones de resistencia al fuego** - al entrar en combate

Todas las pociones de mejora se lanzan a la vez cuando comienza el combate. Los robots vuelven a aplicar mejoras cuando los efectos expiran (quedan menos de 5 segundos).

```mcfunction
/pvpbot settings autopotion true
```

### Retiro
Cuando la salud es baja, los robots se retiran mientras comen o se curan.
La retirada está desactivada si el robot no tiene comida (lucha hasta la muerte).

```mcfunction
/pvpbot settings retreat true
/pvpbot settings retreathp 0.3  # 30% HP
```

---

## 💥 Golpes críticos

Los robots pueden realizar golpes críticos cronometrando sus ataques con saltos.
```mcfunction
/pvpbot settings criticals true
```

---

## 🕸️ Tácticas de telaraña

Los bots pueden utilizar las telarañas estratégicamente:
- **Al retirarse**: coloca una telaraña debajo del enemigo que lo persigue para ralentizarlo.
- **En combate cuerpo a cuerpo** - coloca una telaraña debajo del enemigo que carga

```mcfunction
/pvpbot settings cobweb true
```

---

## ⚙️ Configuración de combate

| Configuración | Gama | Predeterminado | Descripción |
|---------|-------|---------|-------------|
| `combat`| verdadero/falso | verdadero | Habilitar combate |
| `revenge`| verdadero/falso | verdadero | Ataque a quien te atacó |
| `autotarget`| verdadero/falso | falso | Encontrar enemigos automáticamente |
| `criticals`| verdadero/falso | verdadero | Golpes críticos |
| `ranged`| verdadero/falso | verdadero | Utilice arcos |
| `mace`| verdadero/falso | verdadero | Utilice maza |
| `spear`| verdadero/falso | falso | Utilice lanza (buggy) |
| `crystalpvp`| verdadero/falso | falso | Utilice PVP de cristal |
| `anchorpvp`| verdadero/falso | falso | Utilice PVP ancla |
| `elytramace`| verdadero/falso | verdadero | Utilice el truco ElytraMace |
| `autopotion`| verdadero/falso | verdadero | Pociones de uso automático |
| `automend`| verdadero/falso | verdadero | Armadura de reparación automática |
| `menddurability`| 0,1-1,0 | 0,5 | Durabilidad % a reparar |
| `totempriority`| verdadero/falso | verdadero | Tótem sobre escudo |
| `cobweb`| verdadero/falso | verdadero | Utilice telarañas |
| `retreat`| verdadero/falso | verdadero | Retirarse cuando el HP esté bajo |
| `retreathp`| 0,1-0,9 | 0,3 | % de HP para retirarse |
| `attackcooldown`| 1-40 | 10 | Tics entre ataques |
| `meleerange`| 2-6 | 3.5 | Distancia de ataque cuerpo a cuerpo |
| `viewdistance`| 5-128 | 64 | Rango de búsqueda objetivo |
