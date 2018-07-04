class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[] for _ in range(n)]
        for i in range(n):
            dp[i] = [0 for _ in range(m)]
        for i in range(n):
            for j in range(m):
                if i>0 and j>0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                elif i>0 and j==0:
                    dp[i][j] = dp[i-1][j]
                elif i==0 and j>0:
                    dp[i][j] = dp[i][j-1]
                else: dp[i][j] = 1
        return dp[n-1][m-1]
###### can use the way below to generate a list #########
li = [[1]*m]*n
