class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0: return 0
        if int(math.sqrt(n)) ** 2 == n: return 1
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for j in range(1, int(i ** 0.5) + 1):
                if i - j ** 2 >= 0:
                    dp[i] = min(dp[i], dp[i - j**2] + 1)
                else: break
        return dp[n]
