class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1: return len(nums)
        count = 1
        i = 1
        while i<len(nums):
            if nums[i]==nums[i-1]:
                count += 1
            else:
                count = 1
            if count>2:
                del nums[i]
            else: i += 1
        return len(nums)
