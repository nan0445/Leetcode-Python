# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        temp = []
        res = []
        self.s = 0
        def helper(root,s):
            if not root: return
            self.s += root.val
            temp.append(root.val)
            if not root.left and not root.right:
                if self.s==s:
                    res.append(temp[:])
            helper(root.left,s)
            helper(root.right,s)
            self.s -= root.val
            temp.pop()
        helper(root,sum)
        return res
