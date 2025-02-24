"""
LeetCode#189
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

def rotate(nums, k):
    n = len(nums)
    k = k % n
    nums[:] = nums[n-k:] + nums[:n-k]
    return nums
# Test the function
nums = [1,2,3,4,5,6,7]
k = 3
print("Original array: ", nums)
print("Rotated Array: ", rotate(nums, k))  # Output: [5, 6, 7,

