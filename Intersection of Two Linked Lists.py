# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1, p2 = headA, headB
        while p1 and p2:
            if p1==p2: return p1
            p1 = p1.next
            p2 = p2.next
            if not p1 and not p2: return None
            elif not p1: p1 = headB
            elif not p2: p2 = headA
            
