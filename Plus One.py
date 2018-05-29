class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)
        v = 1
        for i in range(0,l):
            v += digits[l-i-1]
            digits[l-i-1] = v%10
            v //= 10
        if v==1:
            digits.insert(0,1)
        return digits
