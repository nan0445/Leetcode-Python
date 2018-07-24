# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = 0
        self.res = 0
        self.flag = False
        def helper(root, k):
            if not root: return
            if self.flag: return
            helper(root.left, k)
            self.count += 1
            if self.count == k:
                self.res = root.val
                self.flag = True
                return
            helper(root.right, k)
        helper(root, k)
        return self.res
