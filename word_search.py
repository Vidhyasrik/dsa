"""
LeetCode#79
Given an mXn grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        m, n = len(board), len(board[0])
        def dfs(i, j, k):
            if k == len(word):
                return True
            if i<0 or i>=m or j<0 or j>=n or board[i]:
                return False
            if board[i][j] != word[k]:
                return False
            board[i][j] = '#'
            res = dfs(i+1, j, k+1) or dfs(i-1,j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
            board[i][j] = word[k]
            return res
        
