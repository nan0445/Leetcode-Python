# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(r1,r2):
            if not r1 and not r2: return True
            if (not r1 and r2) or (not r2 and r1) or (r1.val!=r2.val): return False
            return helper(r1.left,r2.right) and helper(r1.right,r2.left)
        return helper(root,root)
