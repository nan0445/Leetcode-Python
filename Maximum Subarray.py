class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        ans = -2147483648
        for v in nums:
            s += v
            ans = max(ans,s)
            if s<=0:
                s = 0
        return ans
