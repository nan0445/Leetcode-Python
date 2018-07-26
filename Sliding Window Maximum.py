class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums: return []
        res, dp = [], []
        for i in range(len(nums)):
            if dp and dp[0] < i - k + 1:
                dp.pop(0)
            while dp and nums[dp[-1]] < nums[i]:
                dp.pop()
            dp.append(i)
            if i>=k-1:
                res.append(nums[dp[0]])
        return res
