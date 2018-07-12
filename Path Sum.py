# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.s = 0
        self.flag = False
        def helper(root,s):
            if not root: return
            if self.flag: return
            self.s += root.val
            #print(self.s)
            if not root.left and not root.right:
                if self.s==s: self.flag = True
            helper(root.left,s)
            helper(root.right,s)
            self.s -= root.val
        helper(root,sum)
        return self.flag
