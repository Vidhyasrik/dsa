"""
LeetCode#128
Given an unsorted array of integers, nums, return the length of the longest sequence of consecutive elements
"""
def longestConsecutive(nums):
    num_set = set(nums)
    length = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
                length = max(length, current_length)
    return length