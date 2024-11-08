"""
LeetCode#104
"""
# class TreeNode:
#     def __init__(self, val, left, right):
#         self.val = val
#         self.left = left
#         self.right = right
def maxDepth(root):
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return max(left_depth, right_depth) + 1