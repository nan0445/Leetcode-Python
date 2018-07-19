class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1: return 0
        max_nums = max(nums)
        min_nums = min(nums)
        if max_nums == min_nums: return 0
        b = [[] for _ in range(len(nums))]
        l = math.ceil((max_nums - min_nums)/(len(nums)-1))
        for i in range(len(nums)):
            ind = (nums[i] - min_nums)//l
            if not b[ind]: b[ind] = [nums[i], nums[i]]
            else:
                if nums[i]>b[ind][1]: b[ind][1] = nums[i]
                elif nums[i]<b[ind][0]: b[ind][0] = nums[i]
        res = 0
        min_cur = 0
        max_pre = min_nums
        for i in range(len(nums)):
            if b[i]: 
                min_cur = b[i][0]
                res = max(res, min_cur - max_pre)
                max_pre = b[i][1]
        return res
