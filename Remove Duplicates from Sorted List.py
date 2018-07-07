# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = cur = head
        if head==None or head.next==None: return head
        while head:
            if cur.val==head.val:
                cur.next = head.next
            else:
                cur = cur.next
            head = head.next
        return dummy.next
