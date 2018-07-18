class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        words = set(wordDict)
        dp = [[] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i+1):
                if (j==0 or dp[j-1]) and s[j:i+1] in words:
                    dp[i].append(j)
        if not dp[-1]: return []
        
        res = []
        temp = []
        def helper(m):
            if m==-1:
                res.append(' '.join(temp[:][::-1]))
                return
            for i in range(len(dp[m])):
                temp.append(s[dp[m][i]:m+1])
                helper(dp[m][i]-1)
                temp.pop()
                
        helper(len(s)-1)
        return res
