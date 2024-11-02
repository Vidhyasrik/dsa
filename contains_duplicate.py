"""
LeetCode#217
Given an integer array nums, return True if any value appears as least twice in the array, and return False if every element is distinct
"""
def containsDuplicate(nums):
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    return False
# Test the function
print(containsDuplicate([1, 2, 3, 1]))  # True
print(containsDuplicate([1, 2, 3, 4]))  # False
