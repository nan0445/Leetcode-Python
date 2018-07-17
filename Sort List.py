# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        pre = None
        slow = fast = head
        while fast and fast.next:
            pre,slow,fast = slow,slow.next,fast.next.next
        pre.next = None
        l,R = self.sortList(head),self.sortList(slow)
        return self.merge(l,R)
    
    def merge(self,l1,l2):
        dummy = tail = ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                tail.next,l1 = l1,l1.next
            else:
                tail.next,l2 = l2,l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next
        
