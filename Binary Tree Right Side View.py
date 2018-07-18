# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def helper(root,k):
            if not root: return
            if k==0 or k==len(res): res.append([])
            res[k].append(root.val)
            helper(root.left,k+1)
            helper(root.right,k+1)
        helper(root,0)
        ans = []
        for i in range(len(res)):
            ans.append(res[i][-1])
        return ans
