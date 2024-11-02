"""
LeetCode#53
Given an integer array nums, find the subarray with the largest sum, and returns its sum
"""
# Solution#1
def maxSubArray(nums):
    res = nums[0]
    total = 0
    resArr = list()
    for num in nums:
        if total<0:
            resArr.clear()
            total = 0
        total += num
        if total>res:
            resArr.append(num)
        res = max(res, total)
    return res

print("maxSub Array:=>", maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
# Solution#2

def maxSubArray(nums):
    curr_max = 0
    overall_max = float('-inf')
    for num in nums:
        curr_max = max(num, curr_max + num)
        overall_max = max(overall_max, curr_max)
    return overall_max
print("maxSub Array:=>", maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))