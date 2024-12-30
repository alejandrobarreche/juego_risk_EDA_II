import turtle


# Clase para representar las tropas
class Troop:
    def __init__(self, name, cost, strength):
        self.name = name
        self.cost = cost
        self.strength = strength

# Clase para representar un territorio enemigo
class Territory:
    def __init__(self, name, defense, tipo="plano"):
        self.name = name
        self.defense = defense
        self.tipo = tipo

# Clase para gestionar el juego
class RiskGame:
    def __init__(self):
        self.troops = [
            Troop("Infantería", 1, 3),
            Troop("Caballería", 3, 5),
            Troop("Artillería", 5, 7),
        ]
        self.max_resources = 20
        self.territories = [
            Territory("Territorio 1", 10, "montañoso"),
            Territory("Territorio 2", 15, "costero"),
            Territory("Territorio 3", 12, "plano"),
        ]

    def generate_combinations(self):
        def backtrack(combination, resources_left, index):
            if resources_left < 0:
                return

            if index == len(self.troops):
                if all(combination):
                    total_force = sum(combination[i] * self.troops[i].strength for i in range(len(self.troops)))
                    combinations.append({
                        "Infantería": combination[0],
                        "Caballería": combination[1],
                        "Artillería": combination[2],
                        "Fuerza Total": total_force
                    })
                return

            for count in range(resources_left // self.troops[index].cost + 1):
                combination[index] = count
                backtrack(combination, resources_left - count * self.troops[index].cost, index + 1)
                combination[index] = 0

        combinations = []
        backtrack([0] * len(self.troops), self.max_resources, 0)
        return combinations

    def generate_permutations(self):
        def backtrack(path, visited):
            if len(path) == len(self.territories):
                permutations.append(path[:])
                return

            for i, territory in enumerate(self.territories):
                if not visited[i]:
                    visited[i] = True
                    path.append(territory)
                    backtrack(path, visited)
                    path.pop()
                    visited[i] = False

        permutations = []
        backtrack([], [False] * len(self.territories))
        return permutations

    def filter_sorted_permutations(self, permutations):
        filtered = []
        for order in permutations:
            if all(order[i].defense <= order[i + 1].defense for i in range(len(order) - 1)):
                filtered.append(order)
        return filtered

    def evaluate_combinations(self, combinations, territory_orders):
        results = []
        failed_results = []

        terrain_bonus = {
            "montañoso": {"Infantería": 1.2, "Caballería": 0.8, "Artillería": 1.0},
            "costero": {"Infantería": 1.0, "Caballería": 0.8, "Artillería": 1.2},
            "plano": {"Infantería": 1.0, "Caballería": 1.2, "Artillería": 0.8},
        }

        for combo in combinations:
            for order in territory_orders:
                remaining_force = combo["Fuerza Total"]
                conquered_territories = 0
                success = True

                for territory in order:
                    # Ajustar fuerza según tipo de terreno
                    adjusted_force = (
                            combo["Infantería"] * self.troops[0].strength * terrain_bonus[territory.tipo]["Infantería"]
                            + combo["Caballería"] * self.troops[1].strength * terrain_bonus[territory.tipo][
                                "Caballería"]
                            + combo["Artillería"] * self.troops[2].strength * terrain_bonus[territory.tipo][
                                "Artillería"]
                    )

                    if adjusted_force >= territory.defense:
                        remaining_force -= territory.defense
                        conquered_territories += 1
                    else:
                        success = False
                        break

                if conquered_territories == len(order):
                    results.append({
                        "Combinación": combo,
                        "Orden": [t.name for t in order],
                        "Éxito": success,
                    })
                else:
                    failed_results.append({
                        "Combinación": combo,
                        "Conquistados": conquered_territories,
                        "Orden": [t.name for t in order],
                    })

        return results, failed_results

    def maximize_conquests(self, failed_results):
        return max(failed_results, key=lambda x: x["Conquistados"], default=None)

    def display_results(self, results):
        successful_results = [r for r in results if r["Éxito"]]
        print(f"\n=== Resultados Exitosos ===")
        print(f"Total de combinaciones exitosas: {len(successful_results)}\n")
        for i, result in enumerate(successful_results, start=1):
            print(f"Resultado {i}:")
            print(f"- Tropas: Infantería={result['Combinación']['Infantería']}, Caballería={result['Combinación']['Caballería']}, Artillería={result['Combinación']['Artillería']}")
            print(f"- Fuerza Total: {result['Combinación']['Fuerza Total']}")
            print(f"- Orden de Ataque: {' -> '.join(result['Orden'])}")
            print()

    def display_combinations(self, combinations):
        print("\n=== Combinaciones Generadas ===")
        for i, combo in enumerate(combinations, start=1):
            print(f"Combinación {i}: Infantería={combo['Infantería']}, Caballería={combo['Caballería']}, Artillería={combo['Artillería']}, Fuerza Total={combo['Fuerza Total']}")

    def display_permutations(self, permutations):
        print("\n=== Permutaciones Generadas ===")
        for i, perm in enumerate(permutations, start=1):
            print(f"Permutación {i}: {' -> '.join([t.name for t in perm])}")

    def display_filtered_permutations(self, filtered):
        print("\n=== Permutaciones Filtradas De Menor A Mayor ===")
        for i, perm in enumerate(filtered, start=1):
            print(f"Permutación Filtrada {i}: {' -> '.join([t.name for t in perm])}")

    def update_parameters(self):
        print("\n=== Actualización de Parámetros ===")
        self.max_resources = int(input("Introduce el nuevo límite de puntos máximos: "))
        for troop in self.troops:
            troop.cost = int(input(f"Introduce el costo de {troop.name}: "))
            troop.strength = int(input(f"Introduce la fuerza de {troop.name}: "))
        for territory in self.territories:
            territory.defense = int(input(f"Introduce la defensa de {territory.name}: "))

    def run_menu(self):
        while True:
            print("\n=== Menú Principal ===")
            print("1. Generar combinaciones de tropas")
            print("2. Generar permutaciones de territorios")
            print("3. Filtrar permutaciones ordenadas según los puntos del territorio")
            print("4. Evaluar combinaciones y órdenes de ataque")
            print("5. Actualizar parámetros del juego")
            print("6. Salir")

            choice = input("Elige una opción: ")

            if choice == "1":
                combinations = self.generate_combinations()
                self.display_combinations(combinations)
            elif choice == "2":
                permutations = self.generate_permutations()
                self.display_permutations(permutations)
            elif choice == "3":
                permutations = self.generate_permutations()
                filtered = self.filter_sorted_permutations(permutations)
                self.display_filtered_permutations(filtered)
            elif choice == "4":
                combinations = self.generate_combinations()
                permutations = self.generate_permutations()
                filtered = self.filter_sorted_permutations(permutations)
                results, failed = self.evaluate_combinations(combinations, filtered)
                self.display_results(results)
                best_fail = self.maximize_conquests(failed)
                if best_fail:
                    print("\n=== Mejor Intento Fallido ===")
                    print(f"- Tropas: Infantería={best_fail['Combinación']['Infantería']}, Caballería={best_fail['Combinación']['Caballería']}, Artillería={best_fail['Combinación']['Artillería']}")
                    print(f"- Territorios Conquistados: {best_fail['Conquistados']}")
                    print(f"- Orden de Ataque: {' -> '.join(best_fail['Orden'])}")
            elif choice == "5":
                self.update_parameters()
            elif choice == "6":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

class RiskGameWithTurtle(RiskGame):
    def draw_route(self, order, troop_distribution, territory_points):
        # Configuración de la ventana de Turtle
        screen = turtle.Screen()
        screen.title("Recorrido de Ataque")
        screen.bgcolor("white")
        screen.setup(width=800, height=600)

        # Crear el objeto Turtle
        pen = turtle.Turtle()
        pen.shape("turtle")
        pen.speed(2)

        # Posiciones predeterminadas para los territorios
        positions = {
            "Territorio 1": (-300, 200),
            "Territorio 2": (0, -100),
            "Territorio 3": (300, 200),
        }

        # Calcular fuerza inicial total
        total_force = (
            sum(troop_distribution[order[0]].values()) * 3 +
            sum(troop_distribution[order[0]].values()) * 5 +
            sum(troop_distribution[order[0]].values()) * 7
        )
        initial_force = total_force

        # Dibujar los territorios
        pen.penup()
        for name, pos in positions.items():
            pen.goto(pos)
            pen.dot(30, "blue")
            pen.write(name, align="center", font=("Arial", 12, "bold"))

        # Dibujar el recorrido con flechas
        pen.pencolor("red")
        pen.width(2)
        pen.penup()

        for i, territory in enumerate(order):
            x, y = positions[territory]

            if i == 0:
                pen.goto(x, y)
                pen.pendown()
            else:
                pen.goto(x, y)
                pen.stamp()  # Marcar la posición actual

            # Mostrar puntos del territorio
            pen.penup()
            pen.goto(x, y + 40)
            pen.write(f"Puntos: {territory_points[territory]}", align="center", font=("Arial", 10, "bold"))

            # Mostrar tropas y fuerza
            pen.goto(x, y - 40)
            troops = troop_distribution.get(territory, {})
            troop_text = f"I:{troops.get('Infantería', 0)} C:{troops.get('Caballería', 0)} A:{troops.get('Artillería', 0)}"
            pen.write(troop_text, align="center", font=("Arial", 10, "italic"))

            # Calcular fuerza y pérdidas
            adjusted_force = (
                troops.get('Infantería', 0) * 3 +
                troops.get('Caballería', 0) * 5 +
                troops.get('Artillería', 0) * 7
            )
            loss = territory_points[territory]
            total_force -= loss

            # Mostrar fuerza restante y pérdidas
            pen.goto(x, y - 60)
            pen.write(f"Fuerza Restante:  {total_force}", align="center", font=("Arial", 10, "italic"))

            if i < len(order) - 1:
                next_pos = positions[order[i + 1]]
                pen.setheading(pen.towards(next_pos))
                pen.pendown()
                pen.goto(next_pos)

        # Finalizar
        pen.penup()
        pen.hideturtle()
        screen.mainloop()

    def run_menu(self):
        results = []
        failed_results = []

        while True:
            print("\n=== Menú Principal ===")
            print("1. Generar combinaciones de tropas")
            print("2. Generar permutaciones de territorios")
            print("3. Filtrar permutaciones ordenadas según los puntos del territorio")
            print("4. Evaluar combinaciones y órdenes de ataque")
            print("5. Dibujar mejor ruta de ataque")
            print("6. Actualizar parámetros del juego")
            print("7. Salir")

            choice = input("Elige una opción: ")

            if choice == "1":
                combinations = self.generate_combinations()
                self.display_combinations(combinations)
            elif choice == "2":
                permutations = self.generate_permutations()
                self.display_permutations(permutations)
            elif choice == "3":
                permutations = self.generate_permutations()
                filtered = self.filter_sorted_permutations(permutations)
                self.display_filtered_permutations(filtered)
            elif choice == "4":
                combinations = self.generate_combinations()
                permutations = self.generate_permutations()
                filtered = self.filter_sorted_permutations(permutations)
                results, failed_results = self.evaluate_combinations(combinations, filtered)
                self.display_results(results)

                best_fail = self.maximize_conquests(failed_results)
                if best_fail:
                    print("\n=== Mejor Intento Fallido ===")
                    print(f"- Tropas: Infantería={best_fail['Combinación']['Infantería']}, Caballería={best_fail['Combinación']['Caballería']}, Artillería={best_fail['Combinación']['Artillería']}")
                    print(f"- Territorios Conquistados: {best_fail['Conquistados']}")
                    print(f"- Orden de Ataque: {' -> '.join(best_fail['Orden'])}")
            elif choice == "5":
                if results:
                    best_result = results[0]
                    self.draw_route(best_result['Orden'], {
                        territory: {
                            'Infantería': best_result['Combinación']['Infantería'],
                            'Caballería': best_result['Combinación']['Caballería'],
                            'Artillería': best_result['Combinación']['Artillería'],
                        } for territory in best_result['Orden']
                    }, {
                        territory: self.territories[i].defense for i, territory in enumerate(best_result['Orden'])
                    })
                elif failed_results:
                    best_fail = self.maximize_conquests(failed_results)
                    self.draw_route(best_fail['Orden'], {
                        territory: {
                            'Infantería': best_fail['Combinación']['Infantería'],
                            'Caballería': best_fail['Combinación']['Caballería'],
                            'Artillería': best_fail['Combinación']['Artillería'],
                        } for territory in best_fail['Orden']
                    }, {
                        territory: self.territories[i].defense for i, territory in enumerate(best_fail['Orden'])
                    })
                else:
                    print("No se han evaluado combinaciones aún. Por favor, selecciona la opción 4 primero.")
            elif choice == "6":
                self.update_parameters()
            elif choice == "7":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

# Código principal
if __name__ == "__main__":
    game = RiskGameWithTurtle()
    game.run_menu()
