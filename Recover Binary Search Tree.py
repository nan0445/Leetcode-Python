# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.pre,self.n1,self.n2 = None,None,None
        
        def helper(root):
            if not root: return
            helper(root.left)
            if not self.pre: self.pre = root
            if root.val<self.pre.val:
                if not self.n1: self.n1 = self.pre
                self.n2 = root
            self.pre = root
            helper(root.right)
            
        helper(root)
        self.n1.val,self.n2.val = self.n2.val,self.n1.val
