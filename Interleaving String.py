class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1)+len(s2)!=len(s3) or sorted(s1+s2)!=sorted(s3): return False
        dp = {}
        def helper(i,j,k,s1,s2,s3):
            if i==len(s1) and j==len(s2) and k==len(s3): return True
            elif k==len(s3) and (i!=len(s1) or j!=len(s2)): return False
            if (i,j,k) in dp: return dp[(i,j,k)]
            
            if i<len(s1) and s1[i]==s3[k]:
                if helper(i+1,j,k+1,s1,s2,s3): return True
            if j<len(s2) and s2[j]==s3[k]:
                if helper(i,j+1,k+1,s1,s2,s3): return True
            dp[(i,j,k)] = False
            return dp[(i,j,k)]
        return helper(0,0,0,s1,s2,s3)
        
