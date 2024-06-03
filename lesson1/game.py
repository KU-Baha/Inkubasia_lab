from tic_tac_toe.game import TicTacToe, print_board

if __name__ == '__main__':
    board = TicTacToe()
    # some comment
    while True:
        print("Instruction")
        print("The board is 3x3")
        print("Make move by entering row and column number. Column and row number starts from 1")
        print("Player 1: X")
        print("Player 2: O")

        print_board(board.board)

        while not board.winner:
            print(f"Player: {board.current_player.name}")
            row: int = int(input("Row: "))
            col: int = int(input("Col: "))

            board.make_move(row - 1, col - 1)

            board.print_board()

        print(f"Winner: {board.winner}")
        board.finish_the_game()

        play_again = input("Do you want to play again? (y/n): ")

        if play_again.lower() != 'y':
            break
