class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0: return -1
        if target<nums[0] and target>nums[-1]: return -1
        if target==nums[-1]: return len(nums)-1
        if target==nums[0]: return 0
        l, r=0, len(nums)-1
        while l<r:
            mid = (l+r)//2
            if target<nums[mid]:
                if nums[mid]>nums[-1]:
                    if target>nums[0]: r = mid
                    else: l = mid + 1
                else: r = mid
            elif target>nums[mid]:
                if nums[mid]>nums[-1]: l = mid + 1
                else:
                    if target>nums[-1]: r = mid
                    else: l = mid + 1
            else: return mid
        return -1
                
