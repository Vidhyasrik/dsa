"""
LeetCode#242
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once
"""

def isAnagram(s,t):
    if len(s)!=len(t):
        return False
    counter = {}
    for char in s:
        counter[char] = counter.get(char, 0)+1
    for char in t:
        if char not in counter or counter[char] ==0:
            return False
        counter[char] -=1
    return True

# Solution-2
def isAnagram(s,t):
    s_freq = {}
    t_freq = {}
    for char in s:
        s_freq[char] = s_freq.get(char, 0) + 1
    for char in t:
        t_freq[char] = t_freq.get(char, 0) + 1
    return s_freq == t_freq