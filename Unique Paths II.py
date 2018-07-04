class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[1]*n]*m
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i>0 and j==0:
                        dp[i][j] = dp[i-1][j]
                    elif i==0 and j>0:
                        dp[i][j] = dp[i][j-1]
                    elif i>0 and j>0:
                        dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
