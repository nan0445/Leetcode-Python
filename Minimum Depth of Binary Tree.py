# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 2**31-1
        def helper(root,k):
            if not root: return
            if not root.left and not root.right:
                self.res = min(self.res,k)
                return
            helper(root.left,k+1)
            helper(root.right,k+1)
        if not root: return 0
        helper(root,1)
        return self.res
        
