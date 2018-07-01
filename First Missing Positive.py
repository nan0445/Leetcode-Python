class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        ind = [i for i in range(1,l+2)]
        for i in range(l):
            if nums[i] in ind:
                ind.remove(nums[i])
        return ind[0]
