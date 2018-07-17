# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return None
        self.ans = -2**31
        def helper(root):
            if not root: return -2**31
            l = helper(root.left)
            r = helper(root.right)
            t = max(l+root.val,r+root.val,root.val)
            self.ans = max(self.ans,t,l+r+root.val)
            return t
        helper(root)
        return self.ans
        
