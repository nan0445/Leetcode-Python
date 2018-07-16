# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                ans.append(root.val)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return ans
