class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0]<=nums[-1]: return nums[0]
        l, r = 0, len(nums)-1
        while l<r-1:
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l = mid + 1
            else: r = mid 
        return min(nums[l],nums[r])
