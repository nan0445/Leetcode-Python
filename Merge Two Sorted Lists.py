# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dum = res = ListNode(0)
        while l1 or l2:
            if l1 == None:
                res.next = ListNode(l2.val)
                l2 = l2.next
            elif l2 == None:
                res.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val<l2.val:
                res.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val>=l2.val:
                res.next = ListNode(l2.val)
                l2 = l2.next
            res = res.next
        return dum.next
