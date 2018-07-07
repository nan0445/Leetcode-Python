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
        dummy = ans = ListNode(0)
        dummy.next = head
        if head==None or head.next==None: return head
        temp = head.val
        while head.next!=None:
            head = head.next
            if temp==head.val:
                ans.next = head.next
                
            else:
                temp = head.val
                if head.next==None or head.next.val!=ans.next.val:
                    ans = ans.next
        return dummy.next
