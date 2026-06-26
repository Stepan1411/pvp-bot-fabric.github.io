# 🚶 Movement System

PVP Bot presenta un sistema de movimiento avanzado que permite a los robots seguir a los jugadores, escoltar objetivos y navegar a coordenadas específicas.

---

## 🎯 Movement Modes

### Follow Mode
Bots follow a target while maintaining optimal distance.

```mcfunction
# Make bot follow a player
/pvpbot follow Bot1 Steve

# Make bot follow another bot
/pvpbot follow Bot1 Bot2
```

**Behavior:**
- Mantiene una distancia de 3 bloques del objetivo.
- Evita automáticamente los obstáculos.
- Sigue a través de dimensiones
- Uses smart pathfinding
- Se detiene cuando el objetivo está desconectado

### Modo de acompañamiento
Modo de seguimiento mejorado con capacidades defensivas.

```mcfunction
# Make bot escort a player
/pvpbot escort Bot1 Steve

# Make bot escort another bot
/pvpbot escort Bot1 Bot2
```

**Comportamiento:**
- Igual que el modo de seguimiento
- **Defiende automáticamente al objetivo** si es atacado
- Prioriza la protección del objetivo sobre otros combates.
- Ataca a cualquiera que dañe al objetivo escoltado.

### Ir al modo
Movimiento directo basado en coordenadas.

```mcfunction
# Send bot to coordinates
/pvpbot goto Bot1 100 64 200

# Use relative coordinates
/pvpbot goto Bot1 ~10 ~ ~-5
```

**Comportamiento:**
- Búsqueda inteligente de rutas a las coordenadas
- Evitar obstáculos y saltar.
- Integración de barítono opcional
- Se detiene cuando se llega al destino.

---

## 🛑 Detener el movimiento

```mcfunction
# Stop any movement mode
/pvpbot stopmovement Bot1
```

Este comando se detiene:
- Modo de seguimiento
- Modo de escolta
- Ir al modo
- Seguimiento del camino

---

## 👥 Movimiento de facciones

Todos los comandos de movimiento funcionan con facciones:

```mcfunction
# Make entire faction follow a target
/pvpbot faction follow RedTeam Steve

# Make entire faction escort a target
/pvpbot faction escort RedTeam Steve

# Move entire faction to coordinates
/pvpbot faction goto RedTeam 100 64 200
```

---

## ⚙️ Configuración de movimiento

| Configuración | Tipo | Gama | Predeterminado | Descripción |
|---------|------|-------|---------|-------------|
| `movespeed`| doble | 0,1-2,0 | 1.0 | Velocidad de movimiento base |
| `bhop`| booleano | - | verdadero | Habilitar salto de conejo |
| `bhopcooldown`| entero | 5-30 | 12 | Tics entre saltos |
| `jumpboost`| doble | 0,0-0,5 | 0.0 | Altura de salto adicional |
| `gotousebaritone`| booleano | - | falso | Utilice barítono para ir a |

---

## 🧭 Integración de barítono

Habilite Baritone para búsqueda de rutas avanzada:

```mcfunction
/pvpbot settings gotousebaritone true
```

**Beneficios:**
- Navegación por terreno complejo.
- Búsqueda de caminos a larga distancia
- Construcción automática de puentes.
- Minería a través de obstáculos.

**Requisitos:**
- Debe estar instalado el mod Barítono.
- Sólo funciona con comandos goto
- Puede ser más lento que la búsqueda de caminos básica

---

## 🔧 Detalles técnicos

### Seguir distancia
- **Distancia objetivo:** 3 cuadras
- **Distancia de parada:** 2 cuadras
- **Distancia máxima:** 50 bloques (teletransporte si se excede)

### Frecuencia de actualización
- El movimiento se actualiza cada tic (20 veces por segundo)
- La posición del objetivo se comprueba cada 5 tics.
- Pathfinding recalculado cuando sea necesario

### Manejo de obstáculos
- Salto automático sobre obstáculos de 1 bloque.
- Búsqueda de caminos alrededor de muros y barreras.
- Nadar en el agua
- Subir escaleras y enredaderas.

---

## 🚨 Solución de problemas

### Bot no sigue
- Comprobar si el objetivo existe y está en línea
- Verificar que el bot no esté atascado o bloqueado
- Asegúrese de que el movimiento no esté deshabilitado
- Comprobar si el robot está en combate (puede anular el movimiento)

### El robot se atasca
- Usar`/pvpbot stopmovement`y reiniciar
- Habilitar Barítono para terreno complejo
- Compruebe si hay obstáculos que bloqueen el camino.
- Teletransportar al robot para despejar el área.

### Escolta no defiende
- Verificar que el modo acompañante esté activo (no solo seguir)
- Comprobar si el fuego amigo está desactivado.
- Asegúrese de que el bot tenga armas y combate habilitados.
- El objetivo debe recibir daño para activar la defensa.

---

## 💡 Consejos de uso

### Seguimiento efectivo
- Úselo en áreas abiertas para obtener mejores resultados.
- Evite terrenos concurridos o complejos
- Mantenga los objetivos moviéndose a una velocidad razonable.
- Utilice escolta para jugadores importantes.

### Navegación por coordenadas
- Utilice goto para un posicionamiento preciso
- Habilitar Barítono para largas distancias
- Verificar que las coordenadas sean accesibles.
- Utilice coordenadas relativas para el movimiento cercano

### Coordinación de facciones
- Organizar grupos grandes con comandos de facciones.
- Utilice escolta para protección VIP
- Coordinar ataques con la facción goto.
- Distribuya la llegada con comandos escalonados