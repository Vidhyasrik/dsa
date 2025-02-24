"""
LeetCode#290
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, 
such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
"""

def wordPattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    char_to_word, word_to_char = {}, {}
    for c, w in zip(pattern, words):
        if ((c in char_to_word and char_to_word[c] != w) or 
            (w in word_to_char and word_to_char[w] != c)):
            return False
        char_to_word[c] = w
        word_to_char[w] = c
    return True