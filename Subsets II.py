class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        temp = []
        res = []
        def helper(nums,start):
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]: continue
                temp.append(nums[i])
                res.append(temp[:])
                helper(nums,i+1)
                temp.pop()
        helper(nums,0)
        res.append([])
        return res
