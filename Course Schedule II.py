class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        dic = {}
        for i in prerequisites:
            if i[0] not in dic:
                dic[i[0]] = [i[1]]
            else: dic[i[0]].append(i[1])
        visited = [0] * numCourses
        res = []
        def helper(p):
            if visited[p] == -1: 
                return False
            elif visited[p] == 1:
                return True
            visited[p] = -1
            if p in dic:
                for j in dic[p]:
                    if not helper(j): return False
            visited[p] = 1
            res.append(p)
            return True
        
        for i in range(numCourses):
            if not helper(i): return []
        return res
        
################ OR Another way ############################

class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        is_need = [0] * numCourses
        is_pre_need = [[] for _ in range(numCourses)]
        for i in range(len(prerequisites)):
            is_pre_need[prerequisites[i][1]].append(prerequisites[i][0])
            is_need[prerequisites[i][0]] += 1
        no_need = []
        for i in range(numCourses):
            if is_need[i] == 0:
                no_need.append(i)
        res = []
        count = 0
        while no_need:
            x = no_need.pop()
            res.append(x)
            for i in is_pre_need[x]:
                is_need[i] -= 1
                if is_need[i] == 0:
                    no_need.append(i)
            count += 1
        if count == numCourses: return res
        else: return []
