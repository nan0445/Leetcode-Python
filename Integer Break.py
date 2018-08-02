class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2: return 1
        if n == 3: return 2
        x, y = divmod(n, 3)
        if y == 0: return 3**x
        elif y == 2: return 3**x*2
        else: return 3**(x-1) * 4
