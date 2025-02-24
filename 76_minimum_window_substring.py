"""
LeetCode#76
Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character in t 
(including duplicates) is included in the window. If there 
is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.
"""
from collections import defaultdict
def minWindow(s: str, t: str) -> str:
    """
    Given two strings s and t of lengths m and n respectively, 
    return the minimum window substring of s such that every character 
    in t (including duplicates) is included in the window. 
    If there is no such window, return the empty string "".
    Args:
        s: The string to search within.
        t: The target string.
    Returns:
        The minimum window substring of s.
    """
    if not t or not s:
        return ""

    dict_t = defaultdict(int)
    for char in t:
        dict_t[char] += 1

    required = len(dict_t)
    formed = 0
    window_counts = defaultdict(int)

    left, right = 0, 0
    ans = float("inf"), None, None  # length, left, right

    while right < len(s):
        character = s[right]
        window_counts[character] += 1

        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        while left <= right and formed == required:
            character = s[left]

            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)

            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1

            left += 1

        right += 1

    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]