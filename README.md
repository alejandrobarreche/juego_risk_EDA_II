# Risk Game Planning Tool

## Descripción General
Este programa es una herramienta de planificación estratégica basada en el juego de mesa **Risk**. Su objetivo es ayudar a los jugadores a calcular combinaciones de tropas y estrategias óptimas para conquistar territorios enemigos, respetando restricciones de recursos y parámetros configurables.

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
- Identifica combinaciones exitosas que logran conquistar todos los territorios.
- Almacena las combinaciones que no logran conquistar todos los territorios para determinar cuál maximiza las conquistas parciales.

### 5. **Actualización de Parámetros del Juego**
- Permite modificar dinámicamente:
  - Recursos máximos disponibles.
  - Costos y fuerzas de las tropas.
  - Niveles de defensa de los territorios.

### 6. **Menú Interactivo**
- Interfaz en consola que permite al usuario:
  - Generar combinaciones de tropas.
  - Generar y filtrar permutaciones de territorios.
  - Evaluar estrategias de ataque.
  - Actualizar los parámetros del juego.

## Cómo Usarlo
1. Al ejecutar el programa, se mostrará un menú principal en consola con las opciones disponibles.
2. Selecciona una opción introduciendo el número correspondiente.
3. Sigue las instrucciones para interactuar con las diferentes funcionalidades.

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

### **Mejor Intento Fallido:**
```
=== Mejor Intento Fallido ===
- Tropas: Infantería=8, Caballería=1, Artillería=2
- Territorios Conquistados: 2
- Orden de Ataque: Territorio 1 -> Territorio 2 -> Territorio 3
```

## Detalles Técnicos
### Clases Principales
- **`Troop`**: Representa un tipo de tropa, incluyendo su costo y fuerza.
- **`Territory`**: Representa un territorio enemigo con su nivel de defensa.
- **`RiskGame`**: Clase principal que gestiona las combinaciones de tropas, permutaciones de territorios, evaluaciones y parámetros del juego.

### Métodos Clave
- **`generate_combinations`**: Genera combinaciones posibles de tropas.
- **`generate_permutations`**: Genera permutaciones de territorios.
- **`filter_sorted_permutations`**: Filtra las permutaciones para mantener las ordenadas por nivel de defensa.
- **`evaluate_combinations`**: Evalúa combinaciones de tropas contra órdenes de ataque.
- **`maximize_conquests`**: Identifica la mejor combinación parcial en caso de fallos.
- **`update_parameters`**: Actualiza los parámetros del juego.
- **`run_menu`**: Gestiona la interacción del usuario mediante un menú en consola.

## Configuración Inicial
Los valores iniciales del juego son:
- **Tropas**:
  - Infantería: Costo = 1, Fuerza = 3.
  - Caballería: Costo = 3, Fuerza = 3.
  - Artillería: Costo = 5, Fuerza = 3.
- **Recursos máximos disponibles**: 20 puntos.
- **Territorios**:
  - Territorio 1: Defensa = 10.
  - Territorio 2: Defensa = 15.
  - Territorio 3: Defensa = 12.

## Requisitos del Sistema
- Python 3.6 o superior.

## Ejecución
Ejecuta el archivo principal del programa para acceder al menú interactivo:
```bash
python risk_game.py
```
