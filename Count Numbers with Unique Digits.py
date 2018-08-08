class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        def per(x, y):
            if y==0: return 1
            return x * per(x-1, y-1)
        if n>10: n = 10
        res = 1
        for i in range(1,n+1):
            res += 9 * per(9, i-1)
        return res
