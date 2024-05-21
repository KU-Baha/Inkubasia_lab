from .problem_a import counter, is_anagram


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
