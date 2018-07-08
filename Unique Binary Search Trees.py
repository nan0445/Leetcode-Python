class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {0:1, 1:1} 
        
        for i in range(2, n+1):
            dp[i] = sum([dp[i-j-1]*dp[j] for j in range(i)])
        
        return dp[n]
