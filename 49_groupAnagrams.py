"""
LeetCode#49
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""

from collections import defaultdict

def groupAnagrams(strs):
    anagram_groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        anagram_groups[key].append(s)
    return list(anagram_groups.values())

strs = ["eat","tea","tan","ate","nat","bat"]

print("Group Anagrams:=>"*10, groupAnagrams(strs))

# Method#2
def groupAnagrams(strs):
    grouped = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word in grouped:
            grouped[sorted_word].append(word)
        else:
            grouped[sorted_word] = [word]
    return list(grouped.values())
strs = ["eat","tea","tan","ate","nat","bat"]

print("Group Anagrams:=>"*10, groupAnagrams(strs))
