# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return None
        head = UndirectedGraphNode(node.label)
        stack = [node]
        visited = set()
        visited.add(node)
        new = {}
        new[head.label] = head
        
        while stack:
            node = stack.pop()
            new_node = new[node.label]
            for n in node.neighbors:
                if n not in visited:
                    visited.add(n)
                    stack.append(n)
                    new_neighbor = UndirectedGraphNode(n.label)
                    new[n.label] = new_neighbor
                else:
                    new_neighbor = new[n.label]
                new_node.neighbors.append(new_neighbor)
        return head
