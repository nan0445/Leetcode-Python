class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n==0: return []
        count = 0
        ans = [[] for _ in range(n)]
        for i in range(n):
            ans[i] = [0 for _ in range(n)]
        i = 0
        c = 0
        while c<n*n:
            if count%4==0:
                for t in range(count//4,n-count//4):
                    c += 1
                    ans[i][t] = c
                    
            elif count%4==1:
                while i<n-count//4-2:
                    i += 1
                    c += 1
                    ans[i][-1-count//4] = c
                    
            elif count%4==2:
                i += 1
                for t in range(n-count//4-1, -1+count//4, -1):
                    c += 1
                    ans[i][t] = c
            else:
                while i>count//4+1:
                    i -= 1
                    c += 1
                    ans[i][count//4] = c
            count += 1
        return ans
