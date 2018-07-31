class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in range(len(num)):
            if num[0] == '0' and i>0: break
            for j in range(i+1, len(num)):
                if num[i+1] == '0' and j>i+1: break
                flag = False
                s1 = int(num[:i+1])
                s2 = int(num[i+1:j+1])
                s = num[j+1:]
                s3 = str(s1 + s2)
                while len(s3)<=len(s):
                    if s3 != s[:len(s3)]:
                        break
                    flag = True
                    s = s[len(s3):]
                    s1 = s2
                    s2 = int(s3)
                    s3 = str(s1 + s2)
                if not s and flag: return True
        return False
                    
