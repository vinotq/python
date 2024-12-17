from __future__ import annotations
from enum import Enum, auto
from os import system
from abc import ABC


class Triggers(Enum):
    GAME_STARTED = auto()
    P1_initialized = auto()
    P2_initialized = auto()
    SHOT = auto()
    HIT = auto()
    MISSED = auto()
    WIN = auto()


class Validate(ABC):
    def validate(self):
        pass


class ValidateCoordinatesAsNumsWithSpace(Validate):
    def validate(self, str_):
        x, y = str_.split()

        if (len(x) != 1 or len(y) != 1) or (not x.isdigit() or not y.isdigit()):
            return False
        return list(map(int, [x, y]))


class ValidateCoordinatesAsCorrectValues(Validate):
    def validate(self, str_):
        if (not 0 <= int(str_[0]) <= 9) or (not 0 <= int(str_[1]) <= 9):
            return False
        return True


class ValidatePuttingShipInOccupiedSell(Validate):
    def validate(self, str_, board):
        if board[int(str_[0])][int(str_[1])]:
            return False
        return True


class Game:
    def __init__(self, name1: Player, name2: Player):
        self.player1 = name1
        self.player2 = name2
        self.player1.enemy = self.player2
        self.player2.enemy = self.player1
        self.current_player = self.player1
        self.trigger = Triggers.GAME_STARTED

    def validate(self, srt_):
        if not (str_ := ValidateCoordinatesAsNumsWithSpace().validate(srt_)):
            print("Incorrect input! Try to enter your choice like this: 'cord_1 cord_2'.\nSpace is required! Do not put quotes!")
            return False

        if not ValidateCoordinatesAsCorrectValues().validate(str_):
            print("Incorrect input! It is required to enter only values from 0 to 9!")
            return False

        if not ValidatePuttingShipInOccupiedSell().validate(str_, self.current_player.my_board):
            print("This cell is already occupied!")
            return False

        return str_

    def start(self):
        print("Ship placing time!")
        for _ in range(4):
            system("clear")
            self.draw(self.current_player.my_board)

            while not (st := self.validate(input("Input coordinates for your ship: "))):
                pass

            x, y = st
            self.current_player.my_board[y][x] = 1
        self.current_player = self.current_player.enemy

    def shoot(self):
        print("Now shoot time!")
        self.draw(self.current_player.enemy)

        while not (st := self.validateShoot(input("Choose target: "))):
            pass

        self.xy = st
        self.trigger = Triggers.SHOT

    def check(self):
        x, y = self.xy

        if self.current_player.other_board[y][x] == 1:
            self.current_player.enemy.lifes -= 1
            self.current_player.other_board[y][x] = "X"
            self.current_player.my_board[y][x] = "X"
            self.trigger = Triggers.HIT

            if self.lifes == 0:
                self.trigger = Triggers.WIN

        else:
            self.current_player.other_board[y][x] = "O"
            self.current_player.my_board[y][x] = "O"
            self.trigger = Triggers.MISSED

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
    game = Game(Player("Vlad"), Player("Bananov Kirill"))
    game()
