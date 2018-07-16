# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        ans = []
        stack = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            ans.insert(0,cur.val)
            if cur.left: stack.append(cur.left)
            if cur.right: stack.append(cur.right)
        return ans
