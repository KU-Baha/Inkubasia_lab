from problem1 import is_palindrome


# Examples:
#
# Input: 'abccba'
# Output: true
#
# Input: 'dfdfd'
# Output: true
#
# Input: 'abcde'
# Output: false
#
def test_is_palindrome():
    assert is_palindrome('abccba')
    assert is_palindrome('dfdfd')
    assert not is_palindrome('abcde')
