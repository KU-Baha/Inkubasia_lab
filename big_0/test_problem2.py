from problem2 import find_pair_with_given_sum, find_pair_with_given_sum2


def test_find_pair_with_given_sum2():
    assert find_pair_with_given_sum2([1, 7, 10, 12], 8) == (1, 7)
    assert not find_pair_with_given_sum2([2, 3, 4], 1)
    assert find_pair_with_given_sum2([1, 2, 3, 4, 5], 10) == (5, 5)
    assert find_pair_with_given_sum2([1, 2, 3, 4, 5], 9) == (4, 5)
    assert find_pair_with_given_sum2([1, 2, 3, 4, 5], 8) == (3, 5)
    assert find_pair_with_given_sum2([1, 2, 3, 4, 5], 7) == (2, 5)


def test_find_pair_with_given_sum():
    assert find_pair_with_given_sum([1, 7, 10, 12], 8) == (1, 7)
    assert not find_pair_with_given_sum([2, 3, 4], 1)
    assert find_pair_with_given_sum([1, 2, 3, 4, 5], 10) == (5, 5)
    assert find_pair_with_given_sum([1, 2, 3, 4, 5], 9) == (4, 5)
    assert find_pair_with_given_sum([1, 2, 3, 4, 5], 8) == (3, 5)
    assert find_pair_with_given_sum([1, 2, 3, 4, 5], 7) == (2, 5)
