"""
LeetCODE#15
Given an integer array, nums, return  all the triplets [nums[i], nums[j], nums[k]] 
such that i,j,k must be distinct and nums[i] + nums[j] + nums[k]==0. 
The solution set must not contain duplicate elements
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
                                                                  





