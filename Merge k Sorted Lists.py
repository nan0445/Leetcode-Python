# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        temp = []
        for i,v in enumerate(lists):
            while v!=None:
                temp.append(v.val)
                v = v.next
        temp.sort()
        res = dummy = ListNode(0)
        for i in temp:
            res.next = ListNode(i)
            res = res.next
        return dummy.next
        
                
