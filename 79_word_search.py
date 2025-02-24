"""
LeetCode#79
Given an mXn grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells 
are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
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
Solution#
def exist(board,word):
    rows,cols = len(board), len(board[0])
    path = set()
    def dfs(r,c,i):
        if i == len(word):
            return True
        if r<0 or r>=rows or c<0 or c>=cols or word[i]!=board[r][c] or (r,c) in path:
            return False
        path.add((r,c))
        res = (dfs(r+1,c,i+1) or
               dfs(r-1,c,i+1) or
               dfs(r,c+1,i+1) or
               dfs(r,c-1,i+1))
        path.remove((r,c))
        return res
    for r in range(rows):
        for c in range(cols):
            if dfs(r,c,0): return True
    return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

print(exist(board=board, word=word))
        
