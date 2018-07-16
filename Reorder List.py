# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        stack = []
        p1 = p2 = head
        while p1:
            stack.append(p1)
            p1 = p1.next
        count = 0
        if stack: stack.pop(0)
        while stack:
            if count%2==0: p2.next = stack.pop()
            else: p2.next = stack.pop(0)
            #p2.next = stack.pop()
            p2 = p2.next
            p2.next = None
            count += 1
        #p2.next = None
        
