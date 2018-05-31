class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = str(x)
        ab = ""
        if y[0]=="-":
            ab = y[0]
            y = y[1:]
        if y[0] == "0" and len(y)>1:
            y = y[1:]
        res = int(ab+y[::-1])
        return res if res>=-pow(2,31) and res<=pow(2,31)-1 else 0
