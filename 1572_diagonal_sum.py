"""
LeetCode#1572
Given a square matrix mat, return the sum of the matrix diagonals.
Only include the sum of all the elements on the primary diagonal and 
all the elements on the secondary diagonal that are not part of the primary diagonal.
"""

def diagonal_sum(mat: list[list[int]]) -> int:
    n = len(mat) 
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += mat[i][i] 
        if i != n - 1 - i:
            diagonal_sum += mat[i][n - 1 - i]
    return diagonal_sum
# Time complexity: O(n)

