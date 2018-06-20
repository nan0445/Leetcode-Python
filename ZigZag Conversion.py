class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1: return s
        temp = ["" for i in range(numRows)]
        i = 0
        flag = True
        for c in s:
            temp[i]+=c
            if flag: i += 1
            else: i-= 1
            if i==numRows-1: 
                flag = False
            if i==0:
                flag = True
        return "".join(temp)
            
                
            
