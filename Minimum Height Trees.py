class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges: return [0]
        dic = {}
        for v in edges:
            if v[0] not in dic:
                dic[v[0]] = [v[1]]
            else: dic[v[0]].append(v[1])
            if v[1] not in dic: dic[v[1]] = [v[0]]
            else: dic[v[1]].append(v[0])
        visited = [False for _ in range(n)]
        temp, self.res = [], []
        self.l = 0
        def helper(p):
            if visited[p]: return
            visited[p] = True
            if len(temp)>self.l: 
                self.res = temp[:]
                self.l = len(temp)
            for i in dic[p]:
                temp.append(i)
                helper(i)
                temp.pop()
        temp.append(0)
        helper(0)
        #print(self.res[:])
        temp = []
        temp.append(self.res[-1])
        visited = [False for _ in range(n)]
        helper(self.res[-1])
        #print(self.res[:])
        ll = len(self.res)
        if ll%2==0: return [self.res[ll//2-1], self.res[ll//2]]
        else: return [self.res[ll//2]]
                
