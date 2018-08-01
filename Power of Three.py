class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0: return False
        while n>1:
            n, m = divmod(n, 3)
            if m!=0: return False
        return True
