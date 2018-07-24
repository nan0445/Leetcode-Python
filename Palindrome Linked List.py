# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        node = None
        while slow:
            temp = slow.next
            slow.next = node
            node = slow
            slow = temp
        while node and head:
            if node.val!=head.val: return False
            node = node.next
            head = head.next
        return True
        
