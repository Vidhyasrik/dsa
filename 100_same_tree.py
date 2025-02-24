"""
LeetCode#100
Given the root nodes of two binary trees,
return true if they are the same trees. 
two bintree considered same, 
if two trees has same structure and has same values
"""
def isSameTree(p,q):
    if p is None and q is None:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
