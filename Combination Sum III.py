class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        temp, res = [], []
        def helper(k,n,start,l):
            if k == 1 and n in l:
                temp.append(n)
                res.append(temp[:])
                temp.pop()
                return
            for i in range(start,10):
                if n-i<=0: return
                temp.append(i)
                helper(k-1,n-i,i+1,range(i+1,10))
                temp.pop()
                
        helper(k,n,1,[1,10])
        return res
