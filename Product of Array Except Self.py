class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        res[-1] = 1
        for i in range(len(nums)-1)[::-1]:
            res[i] = res[i+1] * nums[i+1]
        s = 1    
        for i in range(len(nums)):
            res[i] *= s
            s *= nums[i]
        return res
