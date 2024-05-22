from .problem_a import counter, is_anagram
from .problem_b import excel_colum


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
