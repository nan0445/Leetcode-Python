class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.helper(nums,[],[])
        
    def helper(self,nums,temp,res):
        if len(temp)==len(nums):
            res.append(temp[:])
            return res
        for i in range(len(nums)):
            if nums[i] in temp:
                continue
            temp.append(nums[i])
            self.helper(nums,temp,res)
            temp.pop()
        return res
    
