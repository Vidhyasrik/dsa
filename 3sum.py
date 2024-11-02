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

print("The Three sum answer is:=>", threesum([1,5,6,7,20],15))

# Solution#3
"""
Given an integer array, nums, return  all the triplets [nums[i], nums[j], nums[k]] such that i,j,k must be distinct and nums[i] + nums[j] + nums[k]==0. The solution set must not contain duplicate elements
"""

def threeSum(nums):
    nums.sort()
    answer = []
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1, len(nums)-1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum < 0:
                left += 1
            elif current_sum > 0:
                right -= 1
            else:
                triplet = [nums[i],nums[left],nums[right]]
                answer.append(triplet)
                while left < right and nums[left] == triplet[1]:
                    left += 1
                while left < right and nums[right] == triplet[2]:
                    right -= 1
    return answer
print("The Three sum answer is:60=>", threeSum([-1,0,1,2]))
print("The Three sum answer is:60=>", threeSum([-4,-2,-1,-1,0,3,5]))
                                                                  





