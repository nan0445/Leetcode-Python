# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        stack = []
        p2 = ListNode(0)
        p1=head
        stack.append(p1)
        p1 = p1.next
        while p1:
            for i in range(len(stack)-1,-1,-1):
                if p1.val>=stack[i].val:
                    stack.insert(i+1,p1)
                    break
            else: stack.insert(0,p1)
            p1 = p1.next
        print([x.val for x in stack])
        p3 = p2
        while stack:
            p3.next = stack.pop(0)
            p3 = p3.next
            p3.next = None
        return p2.next
            



###########Here is the way to switch or insert some node in some place, just need some pointers#################


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p2 = dummy = ListNode(0)
        # pointer 1 points to original list
        p1 = head
        while p1:
            temp = p1.next
            # pointer 2 points to new empty list
            if p1.val < p2.val and p2 is not dummy:
                p2 = dummy
            while p2:
                if not p2.next or p2.next.val >= p1.val:
                    p1.next = p2.next
                    p2.next = p1
                    break
                p2 = p2.next
            p1 = temp
        return dummy.next
