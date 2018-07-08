# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        def helper(root):
            if not root: return
            helper(root.left)
            ans.append(root.val)
            helper(root.right)
            
        helper(root)
        return ans
