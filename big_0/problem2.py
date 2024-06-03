# Problem 1 (easier): Find pair with given sum
#
# Given an array of integers and a target sum, find a pair of integers in the array that adds up to the target. If there’s no such pair of integers in the array, return null (or a similar value depending on the language)
#
# Examples:
#
# Input: [1, 7, 10, 12], target=8
# Output: (1, 7)
#
# Input: [2, 3, 4], target=1
# Output: null
from collections import defaultdict


# Big O(n^2)
def find_pair_with_given_sum(arr: list[int], target: int) -> tuple:
    for i in arr:
        for j in arr:
            if i + j == target:
                return i, j

    return ()


# Big O(n)
def find_pair_with_given_sum2(arr: list[int], target: int) -> tuple:
    hash_table = defaultdict(int)

    for i in arr:
        hash_table[i] += 1

    for i in arr:
        if hash_table.get(target - i):
            return target - i, i

        if hash_table.get(i) == 2 and i * 2 == target:
            return i, i

    return ()


print(find_pair_with_given_sum2([1, 2, 3, 4, 5], 10) == (5, 5))
