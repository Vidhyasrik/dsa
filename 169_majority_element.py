"""
LeetCode#169
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
"""
# Method#1
def majorityElement(nums):
    res, maxCount = 0, 0    
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
        res = num if count[num] > maxCount else res
        maxCount = max(count[num], maxCount)
    return res


print("max Count is:=>", majorityElement([2,2,1,1,1,2,2]))
print("max Count is:=>", majorityElement([3,2,3]))


# Method#2
def majorityElement(nums):
    res, count = 0, 0
    for num in nums:
        if count == 0:
            res = num
        count += (1 if num == res else -1)
    return res


print("max Count is:=>", majorityElement([2,2,1,1,1,2,2]))
print("max Count is:=>", majorityElement([3,2,3]))



