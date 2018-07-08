class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0]=="0": return 0
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(1,len(s)):
            if s[i]=="0" and (int(s[i-1])>2 or s[i-1]=="0"): return 0
            if s[i]=="0": dp[i+1] = dp[i-1]
            else: 
                if int(s[i-1:i+1])<=26 and s[i-1]!="0":
                    dp[i+1] = dp[i] + dp[i-1]
                else: dp[i+1] = dp[i]
        return dp[len(s)]
