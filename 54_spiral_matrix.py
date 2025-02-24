"""
LeetCode#54
Given an m x n matrix, return all elements of the matrix in spiral order.
"""

class Solution:
  def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
    if not matrix:
      return []

    m = len(matrix)
    n = len(matrix[0])
    ans = []
    r1 = 0
    c1 = 0
    r2 = m - 1
    c2 = n - 1

    # Repeatedly add matrix[r1..r2][c1..c2] to `ans`.
    while len(ans) < m * n:
      j = c1
      while j <= c2 and len(ans) < m * n:
        ans.append(matrix[r1][j])
        j += 1
      i = r1 + 1
      while i <= r2 - 1 and len(ans) < m * n:
        ans.append(matrix[i][c2])
        i += 1
      j = c2
      while j >= c1 and len(ans) < m * n:
        ans.append(matrix[r2][j])
        j -= 1
      i = r2 - 1
      while i >= r1 + 1 and len(ans) < m * n:
        ans.append(matrix[i][c1])
        i -= 1
      r1 += 1
      c1 += 1
      r2 -= 1
      c2 -= 1

    return ans
  
print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))

Method2:
def spiral(matrix):
    if not matrix:
        return []
    r1, c1 = 0, 0
    r2, c2 = len(matrix) - 1, len(matrix[0]) - 1
    res = []

    while r1 <= r2 and c1 <= c2:
        # Traverse right
        for j in range(c1, c2 + 1):
            res.append(matrix[r1][j])
        r1 += 1

        # Traverse down
        for i in range(r1, r2 + 1):
            res.append(matrix[i][c2])
        c2 -= 1

        # Traverse left
        if r1 <= r2:  # Check if row still exists
            for j in range(c2, c1 - 1, -1):
                res.append(matrix[r2][j])
            r2 -= 1

        # Traverse up
        if c1 <= c2:  # Check if column still exists
            for i in range(r2, r1 - 1, -1):
                res.append(matrix[i][c1])
            c1 += 1

    return res

print(spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
    