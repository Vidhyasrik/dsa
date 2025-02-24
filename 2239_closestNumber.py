"""
LeetCode#2239
Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.
"""
def findClosestNumber(nums):
    return max(sorted(nums), key=lambda x: (abs(x), -x)) if nums else -1
