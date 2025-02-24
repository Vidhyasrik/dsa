"""
LeetCode#219
Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j in the 
array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

def containsNearbyDuplicate(nums, k):
    num_map = {}
    for i, num in enumerate(nums):
        if num in num_map and i - num_map[num] <= k:
            return True
        num_map[num] = i
    return False