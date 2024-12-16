from __future__ import annotations

from enum import Enum, auto
from os import system


class Triggers(Enum):
    GAME_STARTED = auto()
    P1_initialized = auto()
    P2_initialized = auto()
    SHOT = auto()
    HIT = auto()
    MISSED = auto()
    WIN = auto()


class Game:
    def __init__(self, name1: Player, name2: Player):
        self.player1 = name1
        self.player2 = name2
        self.player1.enemy = self.player2
        self.player2.enemy = self.player1
        self.current_player = self.player1
        self.trigger = Triggers.GAME_STARTED

    def start(self):
        for _ in range(4):
            system("clear")
            self.draw(self.current_player.my_board)
            x, y = -1, -1

            while not (0 <= x <= 9 and 0 <= y <= 9):
                try:
                    coordinates = input("Введите координаты: ")
                    x, y = map(int, coordinates.split())
                except KeyboardInterrupt:
                    exit()
                except Exception:
                    print("Invalid value!!!!!")
            self.current_player.my_board[y][x] = 1
        self.current_player = self.current_player.enemy

    def shoot(self):
        self.draw(self.current_player.other_board)
        x, y = -1, -1

        while not (0 <= x <= 9 and 0 <= y <= 9):
            try:
                coordinates = input("Введите координаты: ")
                x, y = map(int, coordinates.split())

            except KeyboardInterrupt:
                exit()
            except Exception:
                print("Invalid value!")

        self.trigger = Triggers.SHOT

    def check(self):
        pass

    def win(self):
        pass

    def draw(self, board):
        print(self.current_player.name)
        nums = "   " + " ".join([str(i) for i in range(10)])
        print(nums)
        for i in range(10):
            print(i, end=" |")
            for j in range(10):
                print(board[i][j], end="|")
            print()

    def __call__(self):
        while True:
            if self.trigger == Triggers.GAME_STARTED:
                self.start()
                self.trigger = Triggers.P1_initialized
            elif self.trigger == Triggers.P1_initialized:
                self.start()
                self.trigger = Triggers.P2_initialized
            elif self.trigger == Triggers.P2_initialized:
                self.shoot()
            elif self.trigger == Triggers.HIT:
                self.shoot()
            elif self.trigger == Triggers.MISSED:
                self.current_player = self.current_player.enemy
                self.shoot()
            elif self.trigger == Triggers.WIN:
                print(f"Player {self.current_player} won!")
                break
            elif self.trigger == Triggers.SHOT:
                self.check()


class Player:
    def __init__(self, name):
        self.my_board = [[0] * 10 for _ in range(10)]
        self.other_board = [[0] * 10 for _ in range(10)]
        self.enemy = None
        self.lifes = 4
        self.name = name


if __name__ == "__main__":
    game = Game(Player("Vlad;"), Player("Bananov Kirill"))
    game()

