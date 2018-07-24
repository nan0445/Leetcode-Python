class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0: return False
        while n>=2:
            n, m = divmod(n, 2)
            if m != 0: return False
        return True
