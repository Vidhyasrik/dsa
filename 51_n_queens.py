"""
LeetCode#51
The n-queens puzzle is the problem of placing 
n queens on an n x n chessboard such that no two 
queens attack each other.
Given an integer n, return all distinct solutions 
to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' 
placement, where 'Q' and '.' both indicate a queen and an empty space, 
respectively.
"""
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Solves the N-Queens problem.

        Args:
            n: The size of the chessboard.

        Returns:
            A list of lists of strings, where each inner list represents a 
            solution.
        """
        board = [['.' for _ in range(n)] for _ in range(n)]
        solutions = []

        def is_safe(row, col):
            """
            Checks if placing a queen at (row, col) is safe.
            """
            # Check same column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            # Check upper-left diagonal
            i, j = row, col
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            # Check upper-right diagonal
            i, j = row, col
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def solve(row):
            """
            Recursively solves the N-Queens problem.
            """
            if row == n:
                solution = [''.join(row) for row in board]
                solutions.append(solution)
                return

            for col in range(n):
                if is_safe(row, col):
                    board[row][col] = 'Q'
                    solve(row + 1)
                    board[row][col] = '.'  # Backtrack

        solve(0)
        return solutions