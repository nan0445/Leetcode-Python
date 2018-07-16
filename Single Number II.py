class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        flag = False
        if len(nums)==1: return nums[0]
        i = 1
        while i<len(nums):
            if nums[i]!=nums[i-1]:
                if not flag: return nums[i-1]
                else: 
                    flag = False
                    i += 1
            else:
                flag = True
                i += 1
        return nums[-1]
