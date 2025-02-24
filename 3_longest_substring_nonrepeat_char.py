"""
Leetcode#3
Given a string s, find the length of the longest substring without repeating characters.
"""


#solution#1
def lengthOfLongestSubstring(s):
    n = len(s)
    max_length = 0
    seen = {}
    left = 0
    for right in range(n):
        char = s[right]
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        max_length = max(max_length, right - left + 1)
    return max_length


s1 = "abcabcbb"
print(lengthOfLongestSubstring(s1))
