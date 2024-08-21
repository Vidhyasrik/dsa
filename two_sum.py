"""
Leet Code 1
nums is an array, target is an integer return the indices of two numbers that add up to target

Assume that:
Each input has exactly one solution
The same element may not be used twice
"""
def twoSum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        diff = target-nums[i]
        if diff in num_dict:
            return [num_dict[diff], i]
        else:
            num_dict[num] = i
    return []
