"""
LeetCode#2215
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.
"""

def find_disappeared_numbers(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    set1 = set(nums1)  # Use sets for efficient lookups
    set2 = set(nums2)
    not_in_nums2 = list(set1 - set2)
    not_in_nums1 = list(set2 - set1)
    return [not_in_nums2, not_in_nums1]
# Time complexity: O(n + m) where n and m are the sizes of nums1
