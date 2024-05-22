from enum import Enum


# This is an open-ended project, but a chance to get some practice coding.
# The goal is to write a program, in a language of your choice, to let a user play the game tic-tac-toe.
# The type of UI is up to you: try to not spend too much time on the UI,
# but you can have a command-line interface, a web interface, a mobile interface, etc.

# Remember to apply the types of principles we’re discussing in this class!
# Use version control, split up your changes into small commits, write helpful commit messages and test plans.
# You will be graded on how well you write your code and your messages, not on whether the code works.

class Player(Enum):
    FIRST = 'X'
    SECOND = 'O'


class TicTacToe:
    def __init__(self, cols=3, rows=3):
        self.cols = cols
        self.rows = rows
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.current_player = Player.FIRST
        self.winner = None

    def print_board(self):
        ...

    def change_player(self):
        ...

    def set_cell(self, row, col):
        ...
