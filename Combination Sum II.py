class Solution:
    def combinationSum2(self, candidates, target):
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
                if i>ind and candidates[i]==candidates[i-1]: continue
                temp.append(candidates[i])
                helper(candidates,target-candidates[i],i+1)
                temp.pop()
        helper(candidates,target,0)
        return res
