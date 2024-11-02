"""
LeetCode#572
Given the roots of two binary trees root and subRoot, return True if there is a subtree of root with the same structure and node values of subRoot, and False otherwise
"""

def isSubtree(root, subroot):
    if root is None:
        return False
    if isSameTree(root, subroot):
        return True
    return isSubtree(root.left, subroot) or isSubtree(root.right, subroot)
def isSameTree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
                                                                                                       
    