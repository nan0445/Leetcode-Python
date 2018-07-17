class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not s or not t: return 0
        dp = [0 for _ in range(len(t))]
        dic = {}
        for i in range(len(t)):
            if t[i] not in dic:
                dic[t[i]] = [i]
            else: dic[t[i]].insert(0,i)
        for i in range(len(s)):
            if s[i] in t:
                for j in dic[s[i]]:
                    if j == 0: dp[j] += 1
                    else: dp[j] += dp[j-1]
        return dp[-1]
