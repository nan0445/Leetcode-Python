class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dic = {}
        n = sum(int(i)**2 for i in str(n))
        dic[n] = 1
        while n != 1:
            n = sum(int(i)**2 for i in str(n))
            if n in dic and n!=1:
                return False
            dic[n] = 1
            if n == 1: return True
        return True
