class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1
        if dividend<0 and divisor<0:
            sign = 1
        elif dividend<0 or divisor<0:
            sign = -1
        res = 0
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend>=divisor:
            i = 1
            temp = divisor
            while dividend>=temp:
                dividend-=temp
                res+=i
                temp<<=1
                i<<=1
        return min(max(-2147483648, res*sign), 2147483647)
