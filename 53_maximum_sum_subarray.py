"""
LeetCode#53
Given an integer array nums, find the subarray with the largest sum, and returns its sum
"""


# Solution#1
def maxSubArray(nums):
    max_so_far = nums[0]
    curr_max = nums[0]
    for num in nums:
        curr_max = max(num, curr_max + num)  # key DP step
        max_so_far = max(max_so_far, curr_max)
    return max_so_far


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

#Methos#2
def maxSubArray(nums):
    if not nums:
        return 0
    max_sum = float('-inf')
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum