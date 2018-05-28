# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        temp = []
        def helper(root):
            if root == None:
                return
            temp.append(root.val)
            helper(root.right)
            helper(root.left)
        helper(root)
        dic = {}
        for ind, n1 in enumerate(temp):
            n2 = k - n1
            if n2 in dic:
                return True
            else:
                dic[n1] = ind
        return False
#OR
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        nums, n = [root], set()
        for i in nums:
            if k-i.val in n:
                return True
            n.add(i.val)
            if i.left:
                nums.append(i.left)
            if i.right:
                nums.append(i.right)
        return False
