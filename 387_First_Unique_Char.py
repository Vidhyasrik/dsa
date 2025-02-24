"""
LeetCode#387
Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.
"""

from collections import Counter, defaultdict
# Method1
def first_unique_char(s):
    char_counts = Counter(s)
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i
    return -1

print(first_unique_char("ababc"))
# Method2
def first_unique_char(s):
    counter = defaultdict(int)
    for char in s:
        counter[char] += 1
    for i, char in enumerate(s):
        if counter[char] == 1:
            return i
    return -1
print(first_unique_char("ababc"))
