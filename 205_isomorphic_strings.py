"""
LeetCode#3035
Determines if two strings s and t are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character 
while preserving the order of characters. No two characters may map to 
the same character, but a character may map to itself.
Args:
    s: The first string.
    t: The second string.
Returns:
    True if s and t are isomorphic, False otherwise.
"""
#Method#3
def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    mapST, mapTS = {}, {}
    for c1, c2 in zip(s, t):
        if ((c1 in mapST and mapST[c1] != c2) or
            (c2 in mapTS and mapTS[c2] != c1)):
            return False
        mapST[c1] = c2
        mapTS[c2] = c1
    return True
