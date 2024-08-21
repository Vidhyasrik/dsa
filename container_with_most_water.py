#LeetCode#11
#https://leetcode.com/problems/container-with-most-water/
"""
Given an integer array height, where each element represents the height of a potential side of
2D container and each side is 1 unit away from adjacent sides, return the maximum amount of water
that can be stored by choosing two sides to make the container.
"""
class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
    
print("The max water container:=>", Solution().maxArea([2,6,1,5,4]))