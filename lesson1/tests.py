from .problem_a import counter, is_anagram
from .problem_b import excel_colum
from .tic_tac_toe.game import TicTacToe


def test_counter():
    assert counter('ABC') == {'A': 1, 'B': 1, 'C': 1}
    assert counter('BAC') == {'A': 1, 'B': 1, 'C': 1}

    assert counter('stop') == {'s': 1, 't': 1, 'o': 1, 'p': 1}
    assert counter('tops') == {'t': 1, 'o': 1, 'p': 1, 's': 1}

    assert counter('dance') == {'d': 1, 'a': 1, 'n': 1, 'c': 1, 'e': 1}
    assert counter('cancel') == {'c': 2, 'a': 1, 'n': 1, 'e': 1, 'l': 1}


def test_is_anagram():
    assert is_anagram('ABC', "BAC")
    assert is_anagram('stop', 'tops')
    assert not is_anagram('dance', 'cancel')


def test_excel_colum():
    assert excel_colum(1) == 'A'
    assert excel_colum(2) == 'B'

    assert excel_colum(26) == 'Z'
    assert excel_colum(27) == 'AA'
    assert excel_colum(28) == 'AB'

    assert excel_colum(52) == 'AZ'
    assert excel_colum(53) == 'BA'
    assert excel_colum(54) == 'BB'

    assert excel_colum(260) == 'IZ'


def test_game():
    board = TicTacToe()

    assert board.current_player.value == 'X'

    board.make_move(0, 0) # X
    assert board.board == [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    assert board.current_player.value == 'O'

    board.make_move(0, 1) # Y
    assert board.board == [['X', 'O', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    assert board.current_player.value == 'X'

    board.make_move(0, 2) # X
    assert board.board == [['X', 'O', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]

    # Check winner
    board.make_move(1, 2) # Y
    board.make_move(1, 0) # X
    board.make_move(1, 1) # Y
    board.make_move(2, 0) # X

    assert board.winner.value == 'X'

    board.finish_the_game()

    assert board.board == [[' ' for _ in range(3)] for _ in range(3)]
    assert board.current_player.value == 'X'
    assert board.winner is None
