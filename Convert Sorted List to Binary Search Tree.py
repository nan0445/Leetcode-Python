# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        def helper(nums):
            if not nums: return
            mid = len(nums)//2
            root = TreeNode(nums[mid])
            root.left = helper(nums[:mid])
            root.right = helper(nums[mid+1:])
            return root
        return helper(temp[:])
        
