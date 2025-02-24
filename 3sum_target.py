"""
LeetCODE#16
Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to target.
"""
# Solution 1
def threesum(arr,target):
    n = len(arr)
    for i in range(n-1):
        mp = {}
        current_target = target-arr[i]
        for j in range(i+1, n):
            #Check if pair sums to target
            if current_target-arr[j] in mp:
                #Return the founded
                return [arr[i],arr[j],current_target-arr[j]]
            #add element to map
            mp[arr[j]] = j
    return None
print("The Three sum answer is:=>", threesum([1, 5, 6, 7, 3],15))
# Solution#2
def threesum(arr,target):
    arr.sort()
    n=len(arr)
    # result = []
    for i in range(n-2):
        left, right = i+1, n-1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target:
                return [arr[i],arr[left],arr[right]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
print("The Three sum answer is:=>", threesum([1,5,6,7,3],15))
