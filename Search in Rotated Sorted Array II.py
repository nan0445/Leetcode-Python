class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums)==0: return False
        if target<nums[0] and target>nums[-1]: return False
        if target==nums[-1] or target==nums[0]: return True
        
        l, r=0, len(nums)-1
        while l<r:
            mid = (l+r)//2
            if target<nums[mid]:
                if nums[mid]>nums[-1]:
                    if target>nums[0]: r = mid
                    else: l = mid + 1
                elif nums[mid]<nums[-1]: r = mid
                else:
                    for j in range(mid+1, len(nums)):
                        if nums[j]<nums[j-1]: 
                            l = mid + 1
                            break
                    else: r = mid
                            
            elif target>nums[mid]:
                if nums[mid]>nums[-1]: l = mid + 1
                elif nums[mid]<nums[-1]:
                    if target>nums[-1]: r = mid
                    else: l = mid + 1
                else:
                    for j in range(mid+1,len(nums)):
                        if nums[j]>nums[mid]: 
                            l = mid + 1
                            break
                    else: r = mid
            else: return True
        return False
