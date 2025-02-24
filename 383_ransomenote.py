"""
Leetcode#383
Given two strings ransomNote and magazine, return true if ransomNote can be 
constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
"""

#  Method 1: Using dictionaries (character counts)
def canConstruct(ransomNote: str, magazine: str) -> bool:
    ransom_counts = {}
    for char in ransomNote:
        ransom_counts[char] = ransom_counts.get(char, 0) + 1

    magazine_counts = {}
    for char in magazine:
        magazine_counts[char] = magazine_counts.get(char, 0) + 1

    for char, count in ransom_counts.items():
        if magazine_counts.get(char, 0) < count:  # Check if magazine has enough chars
            return False
    return True
print(canConstruct("aa", "aab")) 

# Method 2: Using collections.Counter (more efficient)
from collections import Counter
def canConstruct(ransomNote: str, magazine: str) -> bool:
    ransom_counts = Counter(ransomNote)
    magazine_counts = Counter(magazine)
    return ransom_counts <= magazine_counts
