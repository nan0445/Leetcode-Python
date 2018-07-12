# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder and not inorder: return None
        root = TreeNode(preorder[0])
        ind = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:ind+1],inorder[0:ind])
        root.right = self.buildTree(preorder[ind+1:],inorder[ind+1:])
        return root
