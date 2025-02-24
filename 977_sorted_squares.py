"""
LeetCode#977
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.
"""


def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    index = n-1
    while left <= right:
        if abs(nums[left]) < abs(nums[right]):
            result[index] = nums[right] ** 2
            right -= 1
        else:
            result[index] = nums[left] ** 2
            left += 1
        index -= 1
    return result


nums = [-4, -1, 0, 3, 10]
print("sortedSquares:=>", sortedSquares(nums))