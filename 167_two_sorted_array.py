"""
LeetCode#167
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, 
index1 and index2, added by one as an integer array [index1, index2] of length 2.
"""

def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []   # No solution found


numbers1 = [2, 7, 11, 15]
target1 = 9
print(twoSum(numbers1, target1))  # Output: [1, 2]

numbers2 = [2, 3, 4]
target2 = 6
print(twoSum(numbers2, target2))  # Output: [1, 3]

numbers3 = [-1, 0]
target3 = -1
print(twoSum(numbers3, target3))  # Output: [1, 2]

numbers4 = [1,2,3,4,5]
target4 = 10
print(twoSum(numbers4, target4)) # Output: [4,5]

numbers5 = [1,2,3,4,5]
target5 = 2
print(twoSum(numbers5, target5))  # Output: [1,2]

numbers6 = []
target6 = 0
print(twoSum(numbers6, target6)) # Output: []
