
# Risk Game Planning Tool

## Descripción General
Este programa es una herramienta de planificación estratégica basada en el juego de mesa **Risk**, con funcionalidades ampliadas para visualizar rutas de ataque y evaluar combinaciones de tropas con mayor detalle. Ahora incluye una visualización interactiva utilizando la biblioteca `turtle`.

## Funcionalidades Principales

### 1. **Generación de Combinaciones de Tropas**
- Genera todas las combinaciones posibles de tropas considerando los recursos disponibles.
- Cada combinación incluye:
  - Número de unidades de infantería, caballería y artillería.
  - Fuerza total de las tropas.

### 2. **Generación de Permutaciones de Territorios**
- Crea todas las permutaciones posibles de los territorios enemigos, representando todos los órdenes posibles de ataque.

### 3. **Filtrado de Permutaciones Ordenadas**
- Filtra las permutaciones de territorios para conservar solo aquellas en las que los territorios estén ordenados de menor a mayor según su nivel de defensa.

### 4. **Evaluación de Combinaciones y Órdenes de Ataque**
- Evalúa cada combinación de tropas contra todas las permutaciones de territorios.
- Introduce ajustes en la fuerza basada en bonificaciones específicas según el tipo de terreno:
  - **Montañoso**: Bonus para infantería, penalización para caballería.
  - **Costero**: Bonus para artillería, penalización para caballería.
  - **Plano**: Bonus para caballería, penalización para artillería.
- Identifica combinaciones exitosas y el mejor intento fallido que maximiza las conquistas parciales.

### 5. **Visualización de la Ruta de Ataque**
- Utiliza la biblioteca `turtle` para dibujar la ruta de ataque:
  - Representa los territorios como puntos en un mapa.
  - Muestra los puntos de defensa de cada territorio.
  - Visualiza la distribución de tropas y fuerza restante durante el ataque.

### 6. **Actualización de Parámetros del Juego**
- Permite modificar dinámicamente:
  - Recursos máximos disponibles.
  - Costos y fuerzas de las tropas.
  - Niveles de defensa y tipos de terreno de los territorios.

### 7. **Menú Interactivo**
- Interfaz en consola que permite al usuario:
  - Generar combinaciones de tropas.
  - Generar y filtrar permutaciones de territorios.
  - Evaluar estrategias de ataque.
  - Dibujar rutas de ataque con `turtle`.
  - Actualizar los parámetros del juego.

## Cambios Incorporados
1. **Tipos de Terrenos**:
   - Cada territorio ahora tiene un tipo asociado (`montañoso`, `costero` o `plano`), que afecta las evaluaciones de fuerza.

2. **Visualización con Turtle**:
   - Nueva funcionalidad para dibujar la ruta de ataque en un mapa interactivo, incluyendo información visual sobre tropas, puntos de defensa y fuerza restante.

3. **Bonus de Terreno**:
   - Ajuste de la fuerza de las tropas dependiendo del tipo de terreno del territorio atacado.

4. **Interfaz Ampliada**:
   - Opción adicional en el menú para dibujar la ruta de ataque.

## Ejemplo de Salida
### **Resultados Exitosos:**
```
=== Resultados Exitosos ===
Total de combinaciones exitosas: 2

Resultado 1:
- Tropas: Infantería=11, Caballería=1, Artillería=1
- Fuerza Total: 39
- Orden de Ataque: Territorio 1 -> Territorio 3 -> Territorio 2

Resultado 2:
- Tropas: Infantería=12, Caballería=1, Artillería=1
- Fuerza Total: 42
- Orden de Ataque: Territorio 1 -> Territorio 3 -> Territorio 2
```

### **Ruta de Ataque Visualizada con Turtle**:
- **Territorio 1**:
  - Tropas desplegadas: Infantería=11, Caballería=1, Artillería=1.
  - Puntos de defensa: 10.
  - Fuerza restante tras el ataque: 32.
- **Territorio 2**:
  - Tropas desplegadas: (Calculadas dinámicamente según el resultado).
  - Puntos de defensa: (Mostrados en pantalla).
  - Fuerza restante tras el ataque: (Calculadas en tiempo real).

### **Mejor Intento Fallido:**
```
=== Mejor Intento Fallido ===
- Tropas: Infantería=8, Caballería=1, Artillería=2
- Territorios Conquistados: 2
- Orden de Ataque: Territorio 1 -> Territorio 2 -> Territorio 3
```

## Requisitos del Sistema
- Python 3.6 o superior.
- Biblioteca `turtle` (preinstalada con Python).

## Ejecución
Ejecuta el archivo principal del programa para acceder al menú interactivo:
```bash
python risk_game.py
```
