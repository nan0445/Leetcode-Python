# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helpMe(node, isLeft):  #helper function
            # write your code here using depth first search. 
            # This part is somewhat difficult, refer to online solution if needed.
            if not node: return 0
            if isLeft and not node.left and not node.right: return node.val
            L = helpMe(node.left, True) # write your code here
            R = helpMe(node.right, False) # write your code here
            return L + R
        return helpMe(root, False)
