class Solution:
    dic = {}
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.dic = {}
        return self.helper(nums,[],[],[],"")
        
    def helper(self,nums,temp,ind,res,s):
        if len(temp)==len(nums) and s not in self.dic:
            res.append(temp[:])
            self.dic[s] = 1
            return res
        for i in range(len(nums)):
            if i in ind:
                continue
            ind.append(i)
            temp.append(nums[i])
            s+=str(nums[i])
            self.helper(nums,temp,ind,res,s)
            temp.pop()
            ind.pop()
            s=s[:-1]
            if len(s)>0 and s[-1]=="-": s=s[:-1]
                
        return res
