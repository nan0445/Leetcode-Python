# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        temp = []
        def helper(root):
            if not root: return
            temp.append(str(root.val))
            if not root.left and not root.right:
                res.append('->'.join(temp[:]))
            helper(root.left)
            helper(root.right)
            temp.pop()
        helper(root)
        return res
