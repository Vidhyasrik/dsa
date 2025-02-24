"""
LeetCode#1768
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
"""
def mergeAlternate(w1, w2):
    merged = []
    for a,b in zip(w1, w2):
        merged.append(a + b)
    merged.append(w1[len(w2):])
    merged.append(w2[len(w1):])

    return "".join(merged)

print("mergeAlternative:=>", mergeAlternate("abc", "xyz"))