class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1]
        i, j, k = 0, 0, 0
        while n > 1:
            dp.append(min(dp[i] * 2, dp[j] * 3, dp[k] * 5))
            if dp[-1] % 2 == 0: i += 1
            if dp[-1] % 3 == 0: j += 1
            if dp[-1] % 5 == 0: k += 1
            n -= 1
        return dp[-1]
        
