"""
LeetCode#5
Given a string, return the longest Palindromic substring
"""

def longestPalindrome(s):
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    longest = ""
    for i in range(len(s)):
        # odd length palindrome
        longest = max([longest, expand(i, i)], key=len)
        # even length palindrome
        longest = max([longest, expand(i, i + 1)], key=len)
    return longest

print("Longest Palindrome is:", longestPalindrome('abaab'))