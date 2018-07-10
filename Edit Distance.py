class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[-1 for _ in range(len(word2))] for _ in range(len(word1))]
        
        def helper(word1, word2, ind1, ind2):
            if ind1<0: return ind2+1
            if ind2<0: return ind1+1
            if dp[ind1][ind2] == -1:
                if word1[ind1]==word2[ind2]:
                    dp[ind1][ind2] = helper(word1,word2,ind1-1,ind2-1)
                else:
                    a1 = helper(word1,word2,ind1-1,ind2-1)
                    a2 = helper(word1,word2,ind1,ind2-1)
                    a3 = helper(word1,word2,ind1-1,ind2)
                    dp[ind1][ind2] = min(a1,a2,a3)+1
            return dp[ind1][ind2]
        
        return helper(word1,word2,len(word1)-1,len(word2)-1)
