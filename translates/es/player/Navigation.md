# 🚶 Sistema de navegación

PVP Bot presenta búsqueda de caminos inteligente, mecánicas de movimiento y comandos de movimiento avanzados.

---

## 🎯 Comandos de movimiento

### Seguir el sistema
Los bots pueden seguir a jugadores u otros bots manteniendo una distancia óptima:

```mcfunction
# Make bot follow a target
/pvpbot follow Bot1 Steve

# Stop following
/pvpbot stopmovement Bot1
```

**Comportamiento:**
- Mantiene una distancia de 3 bloques del objetivo.
- Evita automáticamente los obstáculos.
- Sigue el objetivo en todas las dimensiones.
- Utiliza búsqueda de caminos inteligente

### Sistema de acompañamiento
Modo de seguimiento mejorado con capacidades defensivas:

```mcfunction
# Make bot escort (follow + protect) a target
/pvpbot escort Bot1 Steve
```

**Comportamiento:**
- Igual que el modo de seguimiento
- Defiende automáticamente al objetivo si es atacado.
- Prioriza la protección del objetivo sobre otros combates.

### Ir al sistema
Movimiento directo basado en coordenadas:

```mcfunction
# Send bot to specific coordinates
/pvpbot goto Bot1 100 64 200

# Enable Baritone for advanced pathfinding
/pvpbot settings gotousebaritone true
```

**Comportamiento:**
- Búsqueda inteligente de rutas a las coordenadas
- Evitar obstáculos y saltar.
- Integración opcional de barítono para caminos complejos
- Funciona en diferentes tipos de terreno.

---

## 🧭 Búsqueda de caminos

### Evitación de obstáculos
Los bots detectan y evitan automáticamente:
- **Paredes** - Gira a la izquierda/derecha para rodear
- **Agujeros** - Saltar sobre huecos
- **Obstáculos de 1 bloque** - Saltar

### Escalada
Los bots pueden escalar:
- escaleras
- Vides
- Andamios
- Enredaderas retorcidas/lloronas

---

## 🐰 Salto del conejito (Bhop)

Los robots pueden saltar para moverse más rápido: saltar mientras corren para aumentar la velocidad.

```mcfunction
# Enable/disable bhop
/pvpbot settings bhop true

# Set cooldown between jumps (5-30 ticks)
/pvpbot settings bhopcooldown 12

# Add extra jump height (0.0-0.5)
/pvpbot settings jumpboost 0.1
```

### Cuando se activa Bhop
- La velocidad es >= 1,0
- No hay obstáculos por delante
- No escalar
- En el suelo

---

## 😴 Vagabundo inactivo

Cuando los robots no tienen un objetivo, deambulan por su punto de aparición.

```mcfunction
# Enable/disable idle wandering
/pvpbot settings idle true

# Set wander radius (3-50 blocks)
/pvpbot settings idleradius 10
```

### Comportamiento
- Los robots caminan lentamente (no corren)
- Manténgase dentro del radio del punto de generación
- Elige destinos aleatorios
- Evita los obstáculos mientras deambulas.

---

## 🏃 Velocidades de movimiento

Diferentes situaciones utilizan diferentes velocidades:

| Situación | Velocidad | Bhop |
|-----------|---------------|------|
| Vagabundo inactivo | 0,5 | ❌ |
| Acercándose al objetivo | 1.0 | ✅ |
| Comer (retirándose) | 1.2 | ✅ |
| Retiro de HP bajo | 1.5 | ✅ |

---

## ⚙️ Configuración de navegación

| Configuración | Gama | Predeterminado | Descripción |
|---------|-------|---------|-------------|
| `bhop`| verdadero/falso | verdadero | Habilitar salto de conejo |
| `bhopcooldown`| 5-30 | 12 | Tics entre saltos |
| `jumpboost`| 0,0-0,5 | 0.0 | Altura de salto adicional |
| `idle`| verdadero/falso | verdadero | Habilitar deambulación inactiva |
| `idleradius`| 3-50 | 10 | Radio de desplazamiento |
| `movespeed`| 0,1-2,0 | 1.0 | Velocidad de movimiento base |
| `gotousebaritone`| verdadero/falso | falso | Utilice barítono para ir a |

---

## 🔧 Solución de problemas

### El robot se atasca
- Los bots intentan despegarse automáticamente
- Saltan y cambian de dirección después de 10 tics sin movimiento.
- Si aún estás atascado, intenta teletransportar el robot.

### El robot no sube
- Asegúrese de que la escalera/enredadera esté colocada correctamente
- El robot debe estar de cara al bloque escalable.

### Bot cae en agujeros
- Los robots intentan saltar espacios de 2 bloques.
- Los espacios más grandes pueden provocar caídas.
- Considere la posibilidad de construir puentes para caminos importantes.
