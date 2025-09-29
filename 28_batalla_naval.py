import random


# Juego de batalla Naval
class Ship:
    def __init__(self, name: str, size: int):
        self.name: str = name
        self.size: int = size
        self.positions: list[tuple[int, int]] = []
        self.hits: int = 0

    def place(self, x: int, y: int, orientation: str, board: list[list[str]]) -> bool:
        position_aux: list[tuple[int, int]] = []
        # Check if the ship fits on the board
        if orientation == "V":
            if x + self.size > len(board):
                return False
            # Check for collisions before placing the ship
            for i in range(self.size):
                if board[x + i][y] != "*":
                    return False
            # If no collisions, place the ship
            for i in range(self.size):
                board[x + i][y] = self.name[0]
                position_aux.append((x + i, y))
        elif orientation == "H":
            if y + self.size > len(board[0]):
                return False
            # Check for collisions before placing the ship
            for i in range(self.size):
                if board[x][y + i] != "*":
                    return False
            # If no collisions, place the ship
            for i in range(self.size):
                board[x][y + i] = self.name[0]
                position_aux.append((x, y + i))
        else:
            return False

        self.positions = position_aux
        return True

    def hit(self) -> bool:
        self.hits += 1
        return self.hits == self.size


class Destroyer(Ship):
    def __init__(self):
        super().__init__("Destroyer", 2)


class Submarine(Ship):
    def __init__(self):
        super().__init__("Submarine", 3)


class Battleship(Ship):
    def __init__(self):
        super().__init__("Battleship", 4)


class Player:
    def __init__(self, name: str):
        self.name: str = name
        self.ships: list[Ship] = []
        self.board: list[list[str]] = [["*" for _ in range(10)] for _ in range(10)]
        self.hits: list[list[str]] = [["X" for _ in range(10)] for _ in range(10)]

    def place_ship(self, cpu: bool = False):
        ships = [Destroyer(), Submarine(), Battleship()]
        for ship in ships:
            while True:
                print(f"Colocando {ship.name} y tamaño {ship.size}...")
                x = (
                    cpu
                    and random.randint(0, 9)
                    or int(input("Ingrese la coordenada x: "))
                )
                y = (
                    cpu
                    and random.randint(0, 9)
                    or int(input("Ingrese la coordenada y: "))
                )
                orientation = (
                    cpu
                    and random.choice(["H", "V"])
                    or input(
                        "Ingrese la orientación (H para horizontal, V para vertical):"
                    )
                ).upper()
                if ship.place(x, y, orientation, self.board):
                    self.ships.append(ship)
                    self.print_board(self.board)
                    break
                else:
                    print("No se puede colocar el barco en esa posición")

    def print_board(self, board: list[list[str]]):
        for row in board:
            print(" ".join(row))

    def attack(self, opponent: "Player"):
        while True:
            print(f"Atacando a {self.name}...")
            x = int(input("Ingrese la coordenada x: "))
            y = int(input("Ingrese la coordenada y: "))
            if x <= x < len(self.board) and 0 <= y < len(self.board[0]):
                if opponent.board[x][y] == "*":
                    print("Agua 🌊")
                    self.hits[x][y] = "✅"
                    opponent.board[x][y] = "❌"
                elif opponent.board[x][y] != "❌":
                    print("Impacto 🚀")
                    self.hits[x][y] = "💥"
                    for ship in opponent.ships:
                        if (x, y) in ship.positions:
                            if ship.hit():
                                print(f"Has hundido el {ship.name}!")
                                self.ships.remove(ship)
                            break
                    opponent.board[x][y] = "💥"
                    break
                else:
                    print("Ya has atacado esa posición")
            else:
                print("Coordenadas fuera del tablero, intente nuevamente")

    def all_ship_sunk(self):
        return all(ship.hits == ship.size for ship in self.ships)


class BattleShipGame:
    def __init__(self, player1: Player, player2: Player):
        self.player1: Player = player1
        self.player2: Player = player2

    def play(self):
        print("¡Comienza la batalla!")
        print("Jugador 1, coloca tus barcos:")
        self.player1.place_ship()
        print("Jugador 2, coloca tus barcos:")
        self.player2.place_ship(True)

        current_player = self.player1
        opponent = self.player2

        while not self.player1.all_ship_sunk() and not self.player2.all_ship_sunk():
            current_player.attack(opponent)
            if self.player1.all_ship_sunk():
                print(f"{current_player.name} ha ganado!")
                break
            current_player, opponent = opponent, current_player


game = BattleShipGame(Player("Jugador 1"), Player("Jugador 2"))
game.play()
