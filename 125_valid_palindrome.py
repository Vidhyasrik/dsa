"""
LeetCode#125
A phrase is a palindrome if, 
after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""

def isPalindrome(s: str) -> bool:
    """
    Determines if a string is a valid palindrome (ignoring non-alphanumeric characters and case).

    LeetCode 125: Valid Palindrome

    Args:
        s: The input string.

    Returns:
        True if the string is a palindrome, False otherwise.
    """
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1

    return True
# Method#2
def isPalindrome(s: str) -> bool:
    s = ''.join(c for c in s if c.isalnum()).lower()
    return s == s[::-1]
print(isPalindrome("A man, a plan, a canal: Panama"))  # True

