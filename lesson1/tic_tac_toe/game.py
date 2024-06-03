from enum import Enum


# This is an open-ended project, but a chance to get some practice coding.
# The goal is to write a program, in a language of your choice, to let a user play the game tic-tac-toe.
# The type of UI is up to you: try to not spend too much time on the UI,
# but you can have a command-line interface, a web interface, a mobile interface, etc.

# Remember to apply the types of principles we’re discussing in this class!
# Use version control, split up your changes into small commits, write helpful commit messages and test plans.
# You will be graded on how well you write your code and your messages, not on whether the code works.

class PLAYER(Enum):
    FIRST: str = 'X'
    SECOND: str = 'O'


class WINNER(PLAYER):
    DRAW: str = 'Draw'


def print_board(board: list[list[str]]):
    for row in board:
        print('|'.join(row))

    print()


class TicTacToe:
    def __init__(self):
        self.rows = 3
        self.cols: int = 3
        self.board: list[list[str]] = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_player: PLAYER = PLAYER.FIRST
        self.winner: PLAYER.name | str = None

    def change_player(self):
        self.current_player = PLAYER.SECOND if self.current_player == PLAYER.FIRST else PLAYER.FIRST

    def make_move(self, row_num: int, col_num: int):
        if row_num < 0 or col_num < 0 or row_num > 2 or col_num > 2:
            print("Write correct row and col number!")
            print("Try again!")
            print()
            return

        if ' ' != self.board[row_num][col_num]:
            print("This cell is already filled!")
            print("Try again!")
            print()
            return

        self.board[row_num][col_num] = self.current_player.value
        self.check_winner()
        self.change_player()

    def finish_the_game(self):
        self.board: list[list[str]] = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        self.winner = None
        self.current_player = PLAYER.FIRST

    def check_winner(self):
        # check columns
        for col in range(self.cols):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                self.winner = self.current_player
                return

        # check rows
        for row in range(self.rows):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != ' ':
                self.winner = self.current_player
                return

        # check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            self.winner = self.current_player
            return

        # check anti diagonals
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            self.winner = self.current_player
            return

        # check if board is full
        if all([cell != ' ' for row in self.board for cell in row]):
            self.winner = WINNER.DRAW
            return
