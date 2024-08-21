"""
Given a string s, find the length of the longest substring without repeating characters
"""

def lengthOfLongestSubString(s):
    seen = {}
    l=0
    length = 0
    for r in range(len(s)):
        char = s[r]
        if char in seen and seen[char]>=1:
            l = seen[char] + 1
        else:
            length= max(length, r-l+1)
        seen[char] = l
    return length