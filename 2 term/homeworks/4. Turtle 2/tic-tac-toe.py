import math
import turtle as t

from board import Board
from cross import Cross
from inscription import Inscription
from toe import Toe

# set up turtle
t.home()
t.speed(10)
#t.ht()
#t.shape('circle')
t.width(3)

b_size = 400
board = Board(b_size, 2)
board.show()

board = [[None for i in range(3)] for j in range(3)]
coords = [[(i * b_size / 3, j * b_size / 3) for i in range(-1, 2)] for j in range(-1, 2)]

turn = 0
title = Inscription(0, b_size / 2 + 20)
game_result = Inscription(0, b_size / 2 + 40)


def new_game(text):
    global turn

    game_result.hide()
    game_result.set_text(text)
    game_result.show()

    title.hide()
    turn = 0
    title.set_text("Player " + str(turn % 2 + 1) + " turn")
    title.show()

    for i in range(3):
        for j in range(3):
            if board[i][j] is not None:
                board[i][j].hide()
                board[i][j] = None


def check_end_game():
    full = True

    for i in range(3):
        try:
            for j in range(2):
                if board[i][j].get_type() != board[i][j + 1].get_type():
                    break
            else:
                return "\'{}\' wins!".format("X" if board[i][0].get_type() == 1 else "O")
        except AttributeError:
            full = False

    for i in range(3):
        try:
            for j in range(2):
                if board[j][i].get_type() != board[j + 1][i].get_type():
                    break
            else:
                return "\'{}\' wins!".format("X" if board[0][i].get_type() == 1 else "O")
        except AttributeError:
            full = False

    try:
        for i in range(2):
            if board[i][i].get_type() != board[i + 1][i + 1].get_type():
                break
        else:
            return "\'{}\' wins!".format("X" if board[0][0].get_type() == 1 else "O")

        for i in range(2):
            if board[i][2 - i].get_type() != board[i + 1][2 - i - 1].get_type():
                break
        else:
            return "\'{}\' wins!".format("X" if board[0][2].get_type() == 1 else "O")
    except AttributeError:
        full = False

    return "Draw" if full else None


def click_controller(x, y):
    if abs(x) > b_size / 2 or abs(y) > b_size / 2:
        return

    global turn
    m = math.inf
    a = 0
    b = 0
    for i in range(3):
        for j in range(3):
            dist = (x - coords[i][j][0]) ** 2 + (y - coords[i][j][1]) ** 2
            if dist < m:
                a = i
                b = j
                m = dist

    if board[a][b] is None:
        board[a][b] = Cross(*coords[a][b], b_size / 5) if turn % 2 == 0 else Toe(*coords[a][b], b_size / 5)
        board[a][b].show()

        turn += 1
        title.hide()
        title.set_text("Player " + str(turn % 2 + 1) + " turn")
        title.show()

        if check_end_game() is not None:
            new_game(check_end_game())


t.listen()
new_game('')
t.onscreenclick(click_controller, 1)

t.mainloop()
