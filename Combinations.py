class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        temp = []
        res = []
        def helper(t,n):
            if len(temp)==k:
                res.append(temp[:])
                return
            for i in range(t,n+1):
                temp.append(i)
                helper(i+1,n)
                temp.pop()
        helper(1,n)
        return res
