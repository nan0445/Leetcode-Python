class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == n: return m
        i = 0
        while 2**i <= m:
            i += 1
        if n >= 2**(i) or m == 0: return 0
        i -= 1
        res = 2**i
        while i>0:
            m -= 2**i
            n -= 2**i
            while 2**i>m:
                i -= 1
            if n >= 2**(i+1): break
            else: res += 2**i
        return res
########################### OR ###############################
class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ans=n
        while ans>m:
            ans=ans&(ans-1)
        return ans
