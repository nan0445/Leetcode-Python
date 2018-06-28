class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==1:
            return x
        elif n==0:
            return 1
        elif n<0:
            return 1/self.myPow(x,-n)
        elif n%2==0:
            t = self.myPow(x,n/2)
            return t*t
        else:
            return x*self.myPow(x,n-1)
