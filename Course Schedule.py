class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        dic = {}
        for i in prerequisites:
            if i[0] not in dic:
                dic[i[0]] = [i[1]]
            else: dic[i[0]].append(i[1])
        visited = [0] * numCourses
        self.flag = True
        
        def helper(p):
            if visited[p] == -1: 
                self.flag = False
                return
            elif visited[p] == 1:
                return
            visited[p] = -1
            for j in dic[p]:
                if not self.flag: return
                if j in dic: 
                    helper(j)
                    visited[j] = 0
            visited[p] = 1
            
        
        for i in dic:
            helper(i)
            if not self.flag: return False
        return True
            
