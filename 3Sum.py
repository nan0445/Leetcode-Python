class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(0,len(nums)-2):
            if nums[i]>0: return res
            if i>0 and nums[i]==nums[i-1]: continue
            l=i+1
            r=len(nums)-1
            while l<r :
                if nums[l]+nums[r]>-nums[i]:
                    r-=1
                elif nums[l]+nums[r]<-nums[i]:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1] and nums[r]==nums[r+1]:
                        l+=1
        return res
