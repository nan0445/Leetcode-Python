# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.flag = True
        def helper(root):
            if not root: return 0
            if not self.flag: return 0
            l = helper(root.left) 
            r = helper(root.right) 
            if abs(l-r)>1: 
                self.flag = False
                return 0
            return max(l,r)+1
        helper(root)
        return self.flag
                
