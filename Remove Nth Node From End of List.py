# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        dummy = ListNode(0)
        dummy.next = head
        while head!=None:
            head = head.next
            count+=1
        ind = count - n
        res = dummy
        count = 0
        while dummy!=None:
            if count==ind:
                dummy.next = dummy.next.next
                dummy = dummy.next
            else:
                dummy = dummy.next
            count+=1
        return res.next
        
