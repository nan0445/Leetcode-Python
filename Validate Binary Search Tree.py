# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.flag = True
        temp = []
        def helper(root):
            if not root: return
            if not self.flag: return
            helper(root.left)
            if not temp: temp.append(root.val)
            else:
                if root.val<=temp.pop():
                    self.flag = False
                    return
                else: temp.append(root.val)
            helper(root.right)
        helper(root)
        return self.flag
