"""
LeetCode#78
Given an integer array nums of unique elements, 
return all possible subsets
The solution set must not contain duplicate subsets. Return the solution in any order.
"""
from typing import List
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        Generates all possible subsets (the power set) of a list of unique integers.

        LeetCode 78: Subsets

        Args:
            nums: A list of unique integers.

        Returns:
            A list of lists, where each inner list is a subset of nums.
        """
        result = []

        def backtrack(start, current_subset):
            result.append(current_subset[:])  # Add a copy of the current subset

            for i in range(start, len(nums)):
                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()  # Backtrack

        backtrack(0, [])
        return result

# Alternative solution with bit manipulation
class SolutionBitManipulation:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        n = len(nums)

        for i in range(1 << n):  # Iterate through all possible bitmasks (2^n)
            subset = []
            for j in range(n):
                if (i >> j) & 1:  # Check if j-th bit is set
                    subset.append(nums[j])
            result.append(subset)

        return result
############################################################################################
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, curr):
            result.append(curr[:])  # Add a copy of the current subset to the result
            for i in range(start, len(nums)):
                print(f"{start}=>{i}=>{curr}=>{result}")
                curr.append(nums[i])  # Choose the current number
                backtrack(i + 1, curr) 
                # print(f"{i},{curr}") # Explore further subsets
                curr.pop()  # Backtrack: Remove the current number
            # print("completed")
        result = []
        backtrack(0, [])
        return result
# Example usage
nums = [1, 2, 3]
solution = Solution()
subsets = solution.subsets(nums)
print(subsets)