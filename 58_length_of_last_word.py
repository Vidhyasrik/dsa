"""
LeetCode#58
Given a string s consisting of words and spaces, return the length of the last word in the string.
"""

def length_of_last_word(s):
    s = s.strip()  # remove leading and trailing spaces
    words = s.split()  # split the string into words
    if not words:  # if there are no words
        return 0
    return len(words[-1])  # return the length of the last word
