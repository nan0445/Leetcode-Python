# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def helper(m, n):
            if m == n:
                return [TreeNode(m)]
            if m > n:
                return [None]
            ans = []
            for i in range(m, n+1):
                left = helper(m, i-1)
                right = helper(i+1, n)
                for j in range(len(left)):
                    for k in range(len(right)):
                        root = TreeNode(i)
                        root.left = left[j]
                        root.right = right[k]
                        ans.append(root)
            return ans
        
        if n == 0:
            return []
        return helper(1, n)
