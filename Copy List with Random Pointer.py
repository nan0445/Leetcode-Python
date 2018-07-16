# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return None
        new_node = RandomListNode(head.label)
        stack = [head]
        nodes = {new_node.label:new_node}
        visited = set()
        visited.add(head)
        while stack:
            n = stack.pop()
            cur = nodes[n.label]
            if n.next:
                if n.next not in visited:
                    new_node_next = RandomListNode(n.next.label)
                    visited.add(n.next)
                    nodes[new_node_next.label] = new_node_next
                    cur.next = new_node_next
                    stack.append(n.next)
                else:
                    cur.next = nodes[n.next.label]
            if n.random:
                if n.random not in visited:
                    new_node_random = RandomListNode(n.random.label)
                    visited.add(n.random)
                    stack.append(n.random)
                    nodes[new_node_random.label] = new_node_random
                    cur.random = new_node_random
                else:
                    cur.random = nodes[n.random.label]
        return new_node
                    
