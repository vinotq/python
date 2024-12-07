from os import system


class Game:
    def __init__(self) -> None:
        self.board = [[None] * 8 for _ in range(8)]
        self.score = [0, 0]

        for i in range(3):
            for j in range(0, 8, 2):
                self.board[i][j + (i + 1) % 2] = Shashka(0, 0)

        for i in range(5, 8):
            for j in range(0, 8, 2):
                self.board[i][j + (i + 1) % 2] = Shashka(1, 0)

    def draw_board(self):
        system("clear")
        frame = "  A│B│C│D│E│F│G│H│\n" + "─┼" * 8 + "─┤\n"

        for row in range(8):
            frame += str(8 - row) + "│"
            for col in range(8):
                if self.board[row][col]:
                    frame += str(self.board[row][col])
                else:
                    frame += " "
                frame += "│"
            frame += "\n"
            frame += "─┼" * 8 + "─┤"
            frame += "\n"
        print(frame)

    def run(self):
        player = False
        while 12 not in self.score:
            self.draw_board()
            if not player:
                print("[Game] White move!")
            else:
                print("[Game] Black Move!")
            from_pos = input("Choose checker: ")
            x = ord(from_pos[0].upper()) - ord('A')
            y = 7 - ord(from_pos[1]) + ord("1")
            while (
                not 0 <= x <= 7
                or not 0 <= y <= 7
                or not self.board[y][x]
                or self.board[y][x].color != player
            ):
                from_pos = input("Choose checker: ")
                x = ord(from_pos[0].upper()) - ord('A')
                y = 7 - ord(from_pos[1]) + ord("1")

            to_pos = input("Move to: ")
            tx = ord(to_pos[0].upper()) - ord('A')
            ty = 7 - ord(to_pos[1]) + ord("1")
            while (
                not 0 <= tx <= 7
                or not 0 <= ty <= 7
                or self.board[ty][tx]
                or abs(x - tx) != 1
                or y - ty != -1 + 2 * player


            ):
                to_pos = input("Move to: ")
                tx = ord(to_pos[0].upper()) - ord('A')
                ty = 7 - ord(to_pos[1]) + ord("1")

            self.board[ty][tx], self.board[y][x] = self.board[y][x], None
            player = not player


class Shashka:
    def __init__(self, color, condition) -> None:
        self.color = color
        self.condition = condition

    def __str__(self) -> str:
        if self.color == 0:
            return "○"
        return "●"


if __name__ == "__main__":
    game = Game()
    game.draw_board()
    game.run()
