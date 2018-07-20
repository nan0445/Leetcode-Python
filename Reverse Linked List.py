# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            temp = head.next
            head.next = head.next.next
            temp.next = dummy.next
            dummy.next = temp
        return dummy.next
