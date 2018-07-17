class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [2**31-1 for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i+1):
                if s[j:i+1] == s[j:i+1][::-1]:
                    if j==0: dp[i] = 0
                    else: dp[i] = min(dp[i],dp[j-1] + 1)
        return dp[-1]
