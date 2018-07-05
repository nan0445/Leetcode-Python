class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        temp = []
        res = []
        def helper(nums,start):
            for i in range(start,len(nums)):
                temp.append(nums[i])
                res.append(temp[:])
                helper(nums,i+1)
                temp.pop()
        helper(nums,0)
        res.append([])
        return res
