# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head==None or head.next==None: return head
        s,b,small,big = None,None,None,None
        dummy = ListNode(0)
        dummy.next = head
        while head:
            if head.val<x:
                if s==None:
                    small = s = ListNode(head.val)
                else: 
                    s.next = ListNode(head.val)
                    s = s.next
            else:
                if b==None:
                    big = b = ListNode(head.val)
                else:
                    b.next = ListNode(head.val)
                    b = b.next
            head = head.next
        if s!=None: 
            s.next = big
            dummy.next = small
        else: dummy.next = big
        return dummy.next
        
