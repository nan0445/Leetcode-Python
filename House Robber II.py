class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        dp = [0]*len(nums)
        def helper(k):
            for i in range(len(k)):
                if i == 0: dp[i] = k[i]
                elif i == 1: dp[i] = max(k[i-1], k[i])
                else: dp[i] = max(dp[i-1], dp[i-2] + k[i])
            return dp[len(k)-1]
        return max(helper(nums[:-1]), helper(nums[1:]))
        
        
