# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        temp = []
        def helper(root):
            if not root: return
            temp.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        for i in range(len(temp)-1):
            if not root:
                root = TreeNode(temp[i])
            else:
                root.val = temp[i]
            root.left = None
            root.right = TreeNode(temp[i+1])
            root = root.right
        if root: root.right = None
