class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        count = 1
        dummy = x = ListNode(0)
        temp = []
        while count<=n:
            if count<m:
                x.next = ListNode(head.val)
            if count>=m: temp.append(head.val)
            head = head.next
            count += 1
        for i in temp[::-1]:
            x.next = ListNode(i)
            x = x.next
        x.next = head
        return dummy.next
  #### OR switch the orders like below ##########
  class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        start = ListNode(None)
        start.next = head
        prev, node = start, head
        for i in range(1, m):
            node = node.next
            prev = prev.next
        ahead = node.next
        for i in range(m, n):
            tmp = ahead.next
            ahead.next = node
            node, ahead = ahead, tmp
        prev.next.next = ahead
        prev.next = node
        return start.next
