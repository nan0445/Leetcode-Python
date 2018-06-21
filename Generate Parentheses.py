class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def helper(s="", l=0, r=0):
            if len(s)==n*2:
                res.append(s)
                return
            if l<n: helper(s+"(",l+1,r)
            if r<l: helper(s+")",l,r+1)
        helper()
        return res
