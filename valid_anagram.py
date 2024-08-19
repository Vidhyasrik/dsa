"""
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