class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip().split(" ")
        sign = 1
        res = ""
        y = str[0]
        for i in range(0,len(y)):
            if y[i]=="-" and i==0:
                sign = -1
                continue
            elif y[i]=="+" and i==0:
                continue
            if y[i].isdigit():
                res += y[i]
            else:
                break
        if res=="":
            res = 0
        else:
            res = sign*int(res)
        if res<-2**31:
            return -2**31
        elif res>2**31-1:
            return 2**31-1
        else:
            return res
       
