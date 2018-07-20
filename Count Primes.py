class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2: return 0
        d = [1] * n
        d[0] = d[1] = 0
        for i in range(2, int(math.sqrt(n))+1):
            if d[i]:
                d[i**2: n: i] = [0]*len(d[i**2: n: i])
        return sum(d)
                
        
        
