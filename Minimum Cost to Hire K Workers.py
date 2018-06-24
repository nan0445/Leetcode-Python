from heapq import *
import heapq
class Solution:
    
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        l = len(quality)
        ratio = []
        for i in range(l):
        	ratio.append([1.0*quality[i]/wage[i],i])
        ratio.sort(key=lambda x:x[0],reverse=True)
        h = []
        res = 10000*10000*10000
        for i in range(l):
            if i<K:
                heappush(h, -quality[ratio[i][1]])
            else:
                ind = ratio[i][1]
                if quality[ind]<-h[0]:
                    S = S + h[0] + quality[ind]
                    heapreplace(h,-quality[ind])
            if i==K-1:
                S = -sum(h)
            if i>=K-1:
                res = min(res,1.0/ratio[i][0]*S)
        return res
