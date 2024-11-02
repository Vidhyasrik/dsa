"""
LeetCode#100
Given the root nodes of two binary trees,return true if they are the same trees. two bintree considered same, if two trees has same structure and has same values
"""
def isSameTree(p,q):
    if p is None and q is None:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
#time complexity O(n) where n is the number of nodes in the tree
#space complexity O(h) where h is the height of the tree, in the worst case the
# tree is skewed to one side, so h=n. in the average case h=log(n)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
# Example 4:
# Input: p = [1,2,1,null,null,2,3], q =
# [1,2,2,null,null,2,null,null,null,null,3]
# Output: false
# Example 5:
# Input: p = [1,2,1,null,null,2,2], q =
# [1,2,1,null,null,2,2]
# Output: true
# Example 6:
# Input: p = [1,2,1,null,null,2,2], q =
# [1,2,1,null,null,2,2]
# Output: true

