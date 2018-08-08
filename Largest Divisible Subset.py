class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        nums.sort()
        dp = [[num] for num in nums]
        l = 0
        res = [nums[0]]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] % nums[i] == 0 and len(dp[i]) >= len(dp[j]):
                    dp[j] = dp[i] + [nums[j]]
                    if len(dp[j])>l:
                        l = len(dp[j])
                        res = dp[j][:]
        return res
