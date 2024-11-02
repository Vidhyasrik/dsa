"""
LeetCode#14
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""

def longestCommonPrefix(l):
    pref = l[0]
    pref_len = len(pref)

    for s in l[1:]:
        while pref != s[0:pref_len]:
            pref_len -=1
            if pref_len == 0:
                return ""
            pref = pref[0:pref_len]
    return pref

print("LOngest Prefix is:=>", longestCommonPrefix(["flower", "flow", "flight"]))