class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph, stack, res = collections.defaultdict(list), ['JFK'], []
        for a, b in tickets:
            heapq.heappush(graph[a],b)
        while stack:
            if graph[stack[-1]]:
                stack.append(heapq.heappop(graph[stack[-1]]))
            else:
                res.append(stack.pop())
        return res[::-1]
            
