# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        def helper(root,k):
            if not root: return
            if not res or k==len(res): res.append([])
            res[k].append(root.val)
            helper(root.left,k+1)
            helper(root.right,k+1)
        helper(root,0)
        return res[::-1]
