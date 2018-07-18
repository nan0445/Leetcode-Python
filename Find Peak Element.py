class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1: return 0
        l,r = 0, len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]<nums[mid+1]:
                l = mid + 1
            else: r = mid
        return l
