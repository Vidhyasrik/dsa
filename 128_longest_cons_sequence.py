"""
LeetCode#128
Given an unsorted array of integers, nums, return the length of the longest 
sequence of consecutive elements
"""


def longestConsecutive(nums):
    num_set = set(nums)
    length = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
                length = max(length, current_length)
    return length


print(longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # Output: 9
print(longestConsecutive([])) # Output: 0
print(longestConsecutive([1,2,3,4,5])) # Output: 5
print(longestConsecutive([1,2,1,2,3,4,5])) # Output: 5 (duplicates don't affect)
print(longestConsecutive([1,2,3,4,100,200,300])) # Output: 4