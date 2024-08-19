def invertTree(root):
    if not root:
        return
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root
    