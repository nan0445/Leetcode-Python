class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r = 0,len(nums)-1
        if r==-1 or target<nums[0] or target>nums[-1]: return [-1,-1]
        if target == nums[-1]: flag = True
        else: flag = False
        while l<r:
            mid = (l+r)//2
            if target<nums[mid]: r = mid
            elif target>nums[mid]: l = mid + 1
            else:
                l_l,l_r = l, mid
                r_l,r_r = mid,r
                while l_l<l_r:
                    l_mid = (l_l+l_r)//2
                    if target>nums[l_mid]: l_l = l_mid + 1
                    else: l_r = l_mid
                while r_l<r_r:
                    r_mid = (r_l+r_r)//2
                    if target<nums[r_mid]: r_r = r_mid
                    else: r_l = r_mid + 1
                return [l_l, r_l-1] if flag == False else [l_l,len(nums)-1]
        return [-1,-1] if flag==False else [len(nums)-1,len(nums)-1]
