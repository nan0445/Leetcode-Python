class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0,len(nums)-1
        if r==-1: return 0
        while l<r:
            mid = (l+r)//2
            if target>nums[mid]:
                l = mid + 1
            elif target<nums[mid]:
                r = mid
            else: return mid
        if nums[l]>target: return max(l,0)
        elif nums[l]<target: return min(l+1,len(nums))
        elif nums[l]==target: return l
