# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        res = dummy
        while head!=None and head.next!=None:
            dummy.next = ListNode(head.next.val)
            dummy = dummy.next
            dummy.next = ListNode(head.val)
            dummy = dummy.next
            head = head.next.next
        if head!=None:
            dummy.next = ListNode(head.val)
        return res.next
