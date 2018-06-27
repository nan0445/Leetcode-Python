class Solution:
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        candidates.sort()
        def helper(candidates,target,ind):
            if target==0:
                res.append(temp[:])
                return
            
            for i in range(ind,len(candidates)):
                if target-candidates[i]<0: break
                temp.append(candidates[i])
                helper(candidates,target-candidates[i],i)
                temp.pop()
        helper(candidates,target,0)
        return res
