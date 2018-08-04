class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + [i for i in nums if i > 0] + [1]
        l = len(nums)
        dp = [[0]*l for _ in range(l)]
        for x in range(2, l):
            for left in range(0, l-x):
                right = left + x
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][l-1]
         
