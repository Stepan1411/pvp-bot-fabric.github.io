# ⚙️ Configuración

Lista completa de todas las opciones de configuración.

---

## 📋 Comandos

```mcfunction
# Show all settings
/pvpbot settings

# Show specific setting
/pvpbot settings <name>

# Change setting
/pvpbot settings <name> <value>
```

---

## ⚔️ Configuración de combate

| Configuración | Tipo | Gama | Predeterminado | Descripción |
|---------|------|-------|---------|-------------|
| `combat`| booleano | - | verdadero | Activar/desactivar sistema de combate |
| `revenge`| booleano | - | verdadero | Atacan entidades que dañan el bot |
| `autotarget`| booleano | - | falso | Buscar enemigos automáticamente |
| `targetplayers`| booleano | - | verdadero | Puede apuntar a jugadores |
| `targetmobs`| booleano | - | falso | Puede apuntar a turbas hostiles |
| `targetbots`| booleano | - | falso | Puede apuntar a otros robots |
| `criticals`| booleano | - | verdadero | Realizar golpes críticos |
| `ranged`| booleano | - | verdadero | Utilice arcos/ballestas |
| `mace`| booleano | - | verdadero | Utilice maza con cargas de viento |
| `spear`| booleano | - | falso | Usar lanza (deshabilitado debido a un error en la alfombra) |
| `crystalpvp`| booleano | - | falso | Utilice cristal PVP (obsidiana + cristales) |
| `anchorpvp`| booleano | - | falso | Usar ancla PVP (ancla de reaparición + piedra luminosa) |
| `elytramace`| booleano | - | verdadero | Utilice el truco ElytraMace (élytra + maza) |
| `attackcooldown`| entero | 1-40 | 10 | Tics entre ataques |
| `meleerange`| doble | 2-6 | 3.5 | Distancia de ataque cuerpo a cuerpo |
| `movespeed`| doble | 0,1-2,0 | 1.0 | Multiplicador de velocidad de movimiento |
| `viewdistance`| doble | 5-128 | 64 | Rango máximo de detección de objetivos |
| `retreat`| booleano | - | verdadero | Retirarse cuando el HP esté bajo |
| `retreathp`| doble | 0,1-0,9 | 0,3 | Porcentaje de HP para iniciar la retirada (30%) |

---

## 🧪 Configuración de pociones

| Configuración | Tipo | Gama | Predeterminado | Descripción |
|---------|------|-------|---------|-------------|
| `autopotion`| booleano | - | verdadero | Uso automático de pociones curativas/mejoradoras |
| `cobweb`| booleano | - | verdadero | Usa telarañas para ralentizar a los enemigos |

Los bots utilizan automáticamente:
- **Pociones curativas** cuando el HP es bajo
- **Pociones de fuerza** al entrar en combate
- **Pociones de velocidad** al entrar en combate
- **Pociones de resistencia al fuego** al entrar en combate
- **Telarañas** para ralentizar a los enemigos (cuando se retiran o el enemigo carga)

Todas las pociones de mejora se lanzan a la vez cuando comienza el combate o cuando expiran los efectos.

---

## 🚶 Configuración de navegación

| Configuración | Tipo | Gama | Predeterminado | Descripción |
|---------|------|-------|---------|-------------|
| `bhop`| booleano | - | verdadero | Habilitar salto de conejo |
| `bhopcooldown`| entero | 5-30 | 12 | Tics entre saltos de bhop |
| `jumpboost`| doble | 0,0-0,5 | 0.0 | Altura de salto adicional |
| `idle`| booleano | - | verdadero | Deambular cuando no hay objetivo |
| `idleradius`| doble | 3-50 | 10 | Radio de desplazamiento inactivo |

---

## 🛡️ Configuración del equipo

| Configuración | Tipo | Gama | Predeterminado | Descripción |
|---------|------|-------|---------|-------------|
| `autoarmor`| booleano | - | verdadero | Autoequipar la mejor armadura |
| `autoweapon`| booleano | - | verdadero | Autoequipar la mejor arma |
| `autototem`| booleano | - | verdadero | Autoequipar tótem de improviso |
| `totempriority`| booleano | - | verdadero | Priorizar el tótem sobre el escudo |
| `autoshield`| booleano | - | verdadero | Escudo de uso automático al bloquear |
| `automend`| booleano | - | verdadero | Armadura de reparación automática con botellas de XP |
| `menddurability`| doble | 0,1-1,0 | 0,5 | % umbral de durabilidad a reparar (50%) |
| `prefersword`| booleano | - | verdadero | Prefiero la espada al hacha |
| `shieldbreak`| booleano | - | verdadero | Cambia a hacha para romper el escudo enemigo |
| `droparmor`| booleano | - | falso | Suelta piezas de armadura peores |
| `dropweapon`| booleano | - | falso | Tirar armas peores |
| `dropdistance`| doble | 1-10 | 3.0 | Distancia de recogida del artículo |
| `interval`| entero | 1-100 | 20 | Intervalo de verificación del equipo (tics) |
| `minarmorlevel`| entero | 0-100 | 0 | Nivel mínimo de armadura para equipar |

### Niveles de armadura
| Nivel | Tipo de armadura |
|-------|------------|
| 0 | Cualquier armadura |
| 20 | Cuero+ |
| 40 | Oro+ |
| 50 | Cadena+ |
| 60 | Hierro+ |
| 80 | Diamante+ |
| 100 | Sólo Netherita |

---

## 🎭 Configuración de realismo

| Configuración | Tipo | Gama | Predeterminado | Descripción |
|---------|------|-------|---------|-------------|
| `misschance`| entero | 0-100 | 10 | Posibilidad de fallar ataques (%) |
| `mistakechance`| entero | 0-100 | 5 | Posibilidad de atacar en dirección equivocada (%) |
| `reactiondelay`| entero | 0-20 | 0 | Retraso antes de reaccionar (tics) |

---

## 👥 Otras configuraciones

| Configuración | Tipo | Gama | Predeterminado | Descripción |
|---------|------|-------|---------|-------------|
| `factions`| booleano | - | verdadero | Habilitar sistema de facciones |
| `friendlyfire`| booleano | - | falso | Permitir daño a los aliados de las facciones |
| `specialnames`| booleano | - | falso | Utilice nombres especiales de la base de datos |
| `gotousebaritone`| booleano | - | falso | Utilice Barítono para ir a comandos |

---

## 🚀 Configuración de ElytraMace

| Configuración | Tipo | Gama | Predeterminado | Descripción |
|---------|------|-------|---------|-------------|
| `elytramace`| booleano | - | verdadero | Habilitar el truco ElytraMace |
| `elytramaceretries`| entero | 1-10 | 1 | Intentos máximos de reintento de despegue |
| `elytramacealtitude`| entero | 5-50 | 20 | Altitud mínima para el ataque |
| `elytramacedistance`| doble | 3-15 | 8.0 | Distancia de ataque desde el objetivo |
| `elytramacefireworks`| entero | 1-10 | 3 | Número de fuegos artificiales a utilizar |

**Truco de ElytraMace:** Bot equipa los élitros, usa fuegos artificiales para volar, elimina los élitros en el aire y ataca con una maza para causar un daño masivo por caída.

---

## 💾 Archivos de configuración

La configuración se guarda en:
```
config/pvp_bot.json
```

Los datos del bot (posiciones, dimensiones, modos de juego) se guardan en:
```
config/pvp_bot_bots.json
```

Tanto la configuración como los bots persisten tras los reinicios del servidor. Los bots se restauran automáticamente cuando se inicia el servidor.

---

## 📋 Ejemplos

### Haz que los bots sean más realistas
```mcfunction
/pvpbot settings misschance 15
/pvpbot settings mistakechance 10
/pvpbot settings reactiondelay 5
```

### Hacer que los bots sean agresivos
```mcfunction
/pvpbot settings autotarget true
/pvpbot settings targetplayers true
/pvpbot settings targetbots true
/pvpbot settings revenge true
```

### Desactivar el combate a distancia
```mcfunction
/pvpbot settings ranged false
/pvpbot settings mace false
/pvpbot settings crystalpvp false
/pvpbot settings anchorpvp false
```

### Movimiento rápido
```mcfunction
/pvpbot settings bhop true
/pvpbot settings bhopcooldown 8
/pvpbot settings jumpboost 0.2
/pvpbot settings movespeed 1.5
```

### Guardias estacionarias
```mcfunction
/pvpbot settings idle false
/pvpbot settings bhop false
```

### Habilitar el truco ElytraMace
```mcfunction
/pvpbot settings elytramace true
/pvpbot settings elytramacealtitude 25
/pvpbot settings elytramaceretries 2
```

### Habilitar comandos de movimiento con Barítono
```mcfunction
/pvpbot settings gotousebaritone true
```

### Habilitar nombres especiales
```mcfunction
/pvpbot settings specialnames true
```
