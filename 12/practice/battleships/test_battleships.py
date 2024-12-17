from pytest import fixture
from battleships import Game, Player
from sys import stderr


@fixture
def game():
    game = Game(Player("Olegsandr"), Player("Sanya"))
    return game


def grab_input(g):
    def input_(*args):
        print(*args)
        return next(g)
    return input_


def test_correct_coords(monkeypatch, game: Game):
    ls = ['0 0', '0 1', '0 2', '0 3']
    monkeypatch.setattr("builtins.input", grab_input(iter(ls)))

    game.init()

    assert game.player1.my_board[0][0] == 1
    assert game.player1.my_board[1][0] == 1
    assert game.player1.my_board[2][0] == 1
    assert game.player1.my_board[3][0] == 1


def test_incorrect_coords(monkeypatch, capsys, game: Game):
    ls = ['0 0', '0 1', '0 2', '0 3']
    monkeypatch.setattr("builtins.input", grab_input(iter(ls)))

    game.init()
    captured = capsys.readouterr()

    with capsys.disabled():
        print(captured.out)

    lines = captured.out.split('\n')

    assert game.player1.my_board[0][0] == 1
    assert game.player1.my_board[1][0] == 1
    assert game.player1.my_board[2][0] == 1
    assert game.player1.my_board[3][0] == 1


def test_incorrect_ship_coordinates(monkeypatch, game: Game):
    ls = ['0 0', '0 1', '0 2', '1 2']
    monkeypatch.setattr("builtins.input", grab_input(iter(ls)))

    game.init()


def test_incorrect_ship_placing(monkeypatch, game: Game):
    ls = ['0 0', '0 0', '0 1', '0 1']
    monkeypatch.setattr("builtins.input", grab_input(iter(ls)))

    game.init()
