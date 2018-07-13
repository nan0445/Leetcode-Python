class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = []
        for i in range(len(triangle)):
            dp.append([0 for _ in range(i+1)])
            if i==0: dp[i][0] = triangle[i][0]
            else:
                dp[i][0] = triangle[i][0] + dp[i-1][0]
                dp[i][-1] = triangle[i][-1] + dp[i-1][-1]
            for j in range(1,i):
                dp[i][j] = triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j])
        return min(dp[len(triangle)-1])
