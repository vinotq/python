from enum import Enum, auto
from os import system


class Player:
    def __init__(self, name: str = 'default'):
        self.my_board = [[0] * 10 for _ in range(10)]
        self.enemy_board = [[0] * 10 for _ in range(10)]
        self.enemy = None
        self.name = name
        self.score = 4
        self.name = name


class Trigger(Enum):
    GAME_STARTED = auto()
    P1_INITED = auto()
    P2_INITED = auto()
    SHOT = auto()
    HIT = auto()
    MISSED = auto()
    WIN = auto()


class Game:
    def __init__(self, pl1: Player, pl2: Player):
        self.player1 = pl1
        self.player2 = pl2
        self.player1.enemy = self.player2
        self.player2.enemy = self.player1
        self.current_player = self.player1
        self.trigger = Trigger.GAME_STARTED

    def draw(self, player: Player):
        res = ''
        cells = "□▦▪️"
        for i in range(10):
            for j in range(10):
                res += cells[player.my_board[i][j]]
            res += '\n'
        print(res)

    def init(self):
        for _ in range(4):
            system("clear")
            self.draw(self.current_player)
            x, y = -1, -1
            while not (0 <= x <= 9) or not (0 <= y <= 9):
                try:
                    pos = input("Enter pos: ")
                    x, y = map(int, pos.split())
                except KeyboardInterrupt:
                    exit()
                except Exception:
                    print("Invalid")
            self.current_player.my_board[y][x] = 1
        self.current_player = self.current_player.enemy

    def shoot():
        ...

    def check():
        ...

    def win():
        ...

    def __call__(self):
        while True:
            match self.trigger:
                case Trigger.GAME_STARTED:
                    self.init()
                case Trigger.P1_INITED:
                    self.init()
                case Trigger.P2_INITED:
                    self.shoot()
                case Trigger.SHOT:
                    self.check()
                case Trigger.HIT:
                    self.shoot()
                case Trigger.MISSED:
                    self.current_player = self.current_player.enemy
                    self.shoot()
                case Trigger.WIN:
                    self.win()
                    break
                case _:
                    ...


if __name__ == "__main__":
    g = Game(Player(), Player())
    g()

