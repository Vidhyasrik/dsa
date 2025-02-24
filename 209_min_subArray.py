"""
Leetcode#209
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""

def minSubArrayLen(target, nums):
    n = len(nums)
    if n == 0:
        return 0

    min_len = float('inf')  # Initialize with infinity
    left = 0
    current_sum = 0
    for right in range(n):
        current_sum += nums[right]
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)  # Update min_len
            current_sum -= nums[left]  # Shrink the window from the left
            left += 1
    return min_len if min_len != float('inf') else 0


print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # Output: 2
print(minSubArrayLen(4, [1, 4, 4]))  # Output: 1
print(minSubArrayLen(11, [1, 2, 3, 4, 5]))  # Output: 3
print(minSubArrayLen(15, [1, 2, 3, 4, 5]))  # Output: 5
print(minSubArrayLen(4, [1, 2, 1, 2]))  # Output: 2