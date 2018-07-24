# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def helper(root):
            if not root: return
            root.left, root.right = root.right, root.left
            helper(root.left)
            helper(root.right)
        helper(root)
        return root
