class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l<=1: return 0
        dp = [0 for _ in range(l)]
        for i in range(l):
            t = min(l-1,i+nums[i])
            if dp[l-1]!=0: return dp[l-1]
            for j in range(t,i,-1):
                if dp[j]==0: dp[j] = dp[i]+1
                else:
                    break
        return dp[l-1]
