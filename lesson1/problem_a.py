from collections import defaultdict


# Write a function to determine whether two given strings are “anagrams”
# (you can rearrange the letters of one to form the other).

# Examples:
# “ABC” and “BAC”: true
# “stop” and “tops”: true
# “dance” and “cancel”: false


def counter(val):
    result = defaultdict(int)

    for i in val:
        result[i] += 1

    return result


def is_anagram(val1, val2):
    val1 = counter(val1)
    val2 = counter(val2)
    return val1 == val2
