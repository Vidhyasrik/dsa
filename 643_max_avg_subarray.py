"""
LeetcOde#643
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.
"""


def findMaxAverage(nums, k):
    n = len(nums)
    if n < k:
        return 0.0
    current_sum = sum(nums[:k])
    max_sum = current_sum/k
    for i in range(k, n):
        current_sum = current_sum - nums[i-k] + nums[i]
        max_sum = max(max_sum, current_sum/k)
    return max_sum


nums = [1, 12, -5, -6, 50, 3]
k = 4
print(findMaxAverage(nums, k))  # Output: 12.75