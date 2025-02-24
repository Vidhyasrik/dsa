"""
LeetCode#26
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
    Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
    Return k.
"""

def remove_duplicates(nums):
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1
# Test the function
nums = [1, 1, 2, 2, 3, 3]
print(remove_duplicates(nums))  # Output: 3
nums = [1,1,2]
print(remove_duplicates(nums))  # Output: 2
nums = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicates(nums))  # Output: 5
