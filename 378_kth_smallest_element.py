"""
LeetCode#378
Given an n x n matrix where each of the rows and columns is 
sorted in ascending order, return the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, 
not the kth distinct element.
You must find a solution with a memory complexity better than O(n2).
"""
import heapq

def kthSmallest(matrix, k):
    """
    Finds the kth smallest element in a sorted matrix.

    LeetCode 378: Kth Smallest Element in a Sorted Matrix

    Args:
        matrix: A list of lists of integers (n x n sorted matrix).
        k: The kth smallest element to find.

    Returns:
        The kth smallest element in the matrix.
    """
    n = len(matrix)
    min_heap = []

    # Push the first element of each row into the min-heap
    for r in range(n):
        heapq.heappush(min_heap, (matrix[r][0], r, 0))  # (value, row, col)

    # Pop k-1 elements from the min-heap
    for _ in range(k - 1):
        val, r, c = heapq.heappop(min_heap)
        if c + 1 < n:
            heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))

    # The kth smallest element is now at the top of the min-heap
    return heapq.heappop(min_heap)[0]

