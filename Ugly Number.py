class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        if num == 1: return True
        while num > 5:
            if num % 2 != 0 and num % 3 != 0 and num % 5 != 0: return False
            if num % 2 == 0: num /= 2
            elif num % 3 == 0: num /= 3
            else: num /= 5
        return True
