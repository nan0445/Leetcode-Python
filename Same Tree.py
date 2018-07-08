# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        self.flag = True
        self.p = False
        def helper(p,q):
            if not p and not q: return
            if not p or not q: 
                self.flag = False
                self.p = True
                return
            if self.p: return
            if p.val!=q.val:
                self.flag = False
                self.p = True
                return
            helper(p.left, q.left)
            helper(p.right, q.right)
            
        helper(p,q)
        return self.flag
