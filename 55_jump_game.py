"""
LeetCode#55
You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
"""

def can_jump(nums):
    n = len(nums)
    if n <= 1: 
        return True
    max_reach = 0
    for i in range(n):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
        if max_reach >= n - 1:
            return True
    return False


nums1 = [2, 3, 1, 1, 4]
print(f"Can jump for nums1: {can_jump(nums1)}")  # Output: True
nums2 = [3, 2, 1, 0, 4]
print(f"Can jump for nums2: {can_jump(nums2)}")  # Output: False

nums3 = [0]
print(f"Can jump for nums3: {can_jump(nums3)}")  # Output: True

nums4 = [0,1]
print(f"Can jump for nums4: {can_jump(nums4)}")  # Output: False

nums5 = [2,0,0]
print(f"Can jump for nums5: {can_jump(nums5)}")  # Output: True

nums6 = [2,5,0,0,1,1]
print(f"Can jump for nums6: {can_jump(nums6)}")  # Output: True

