class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = nums[0]+nums[1]+nums[2]
        ab = abs(res-target)
        print (nums)
        for i in range(len(nums)-2):
            if nums[i]+nums[i+1]+nums[i+2]>target:
                if abs(nums[i]+nums[i+1]+nums[i+2]-target)<ab:
                    return nums[i]+nums[i+1]+nums[i+2]
            l = i+1
            r = len(nums)-1
            #temp_ab = abs(nums[i]+nums[l]+nums[r]-target)
            while l<r:
                temp = nums[i]+nums[l]+nums[r]
                if temp>target:
                    r-=1
                elif temp<target:
                    l+=1
                else:
                    return target
                if abs(temp-target)<ab:
                    res = temp
                    ab = abs(temp-target)
            
        return res
