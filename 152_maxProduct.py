"""
LeetCode152
Given an integer array nums, find a subarray that has the largest product, 
and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
"""

def maxProduct(nums):
    """
    Finds the contiguous subarray within nums which has the largest product.
    Args:
        nums: A list of integers.
    Returns:
        The largest product of a contiguous subarray.
    """

    if not nums:
        return 0

    max_so_far = nums[0]
    min_so_far = nums[0]
    result = max_so_far

    for i in range(1, len(nums)):
        curr = nums[i]
        temp_max = max(curr, max_so_far * curr, min_so_far * curr)
        min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
        max_so_far = temp_max

        result = max(result, max_so_far)

    return result

print("Result:=>"*10, maxProduct([2,3,-2,4]))
print("Result:=>"*10, maxProduct([-2,0,-1]))
print("Result:=>"*10, maxProduct([-2]))
print("Result:=>"*10, maxProduct([-3,-1,-1]))
print("Result:=>"*10, maxProduct([2,3,-2,4,-2]))
print("Result:=>"*10, maxProduct([0,2]))