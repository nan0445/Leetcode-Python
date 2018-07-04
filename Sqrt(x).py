class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0 or x==1: return x
        l, r = 1, x
        while l<r:
            mid = (r+l)//2
            if mid**2>x:
                r = mid
            elif mid**2<x:
                l = mid + 1
            else: return mid
        if l*l<=x: return l
        else: return l-1
