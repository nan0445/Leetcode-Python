# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        l, r = 1, 1
        r1 = r2 = root
        while r1.left or r2.right:
            if r1.left:
                r1 = r1.left
                l += 1
            if r2.right:
                r2 = r2.right
                r += 1
        if l==r: return 2**l-1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
