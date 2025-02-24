"""
LeetCode#226
Given the root of a binary tree, invert the tree, and return its root.
"""
def invertTree(root):
    if not root:
        return
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root
    