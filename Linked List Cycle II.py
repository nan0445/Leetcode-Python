# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        slow = fast = head
        stack = set()
        stack.add(slow)
        flag = False
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            stack.add(slow)
            if slow==fast:
                flag = True
                break
            
            
        if not flag: return None
        if slow==head: return head
        slow = slow.next
        while slow not in stack:
            slow = slow.next
        return slow
                
