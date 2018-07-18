class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        temp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ans = ''
        while n>0:
            n, m = divmod(n-1, 26)
            ans = temp[m] + ans
        return ans
