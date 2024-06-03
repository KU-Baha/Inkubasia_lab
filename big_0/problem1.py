# Problem 1 (easiest): Is palindrome
#
# Given a string, determine whether it’s a palindrome (the string is the same if you reverse it).

# Big O(n)
def is_palindrome(text: str) -> bool:
    return text == text[::-1]
