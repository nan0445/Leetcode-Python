# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node):
            if not node: return 0,0
            l, r = helper(node.left), helper(node.right)
            return max(l) + max(r), node.val + l[0] + r[0]
        return max(helper(root))
