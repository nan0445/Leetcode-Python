class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_pre = nums[:]
        max_pre = nums[:]
        for i in range(1,len(nums)):
            cur = [min_pre[i-1]*nums[i], max_pre[i-1]*nums[i], nums[i]]
            max_pre[i] = max(cur)
            min_pre[i] = min(cur)
        return max(max_pre)
