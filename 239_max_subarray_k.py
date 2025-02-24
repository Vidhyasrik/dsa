"""
LeetCode#239
You are given an array of integers nums, 
there is a sliding window of size k which is moving from 
the very left of the array to the very right. 
You can only see the k numbers in the window. 
Each time the sliding window moves right by one position.
Return the max sliding window.
"""

def max_subarray_k(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return []

    result = []
    for i in range(len(arr) - k + 1):
        subarray = arr[i:i + k]
        result.append(max(subarray))

    return result
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
max_values = max_subarray_k(arr, k)
print(max_values)  # Output: [3, 3, 5, 5, 6, 7]

arr = [10, 5, 2, 7, 8, 7]
max_values = max_subarray_k(arr, k)
print(max_values)  
