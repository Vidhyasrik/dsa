"""
LeetCode#28
Given two strings needle and haystack, 
return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.
"""


def strStr(haystack, needle):
    if not needle:
        return 0
    n = len(haystack)
    m = len(needle)
    if m > n:
        return -1
    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:
            return i
    return -1


def strStr(haystack, needle):
    if needle == "":
        return 0
    if needle not in haystack:
        return -1
    return haystack.index(needle)  # return the index of the first occurrence of needle in haystack

