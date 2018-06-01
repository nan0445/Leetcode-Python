class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        for i in range(0,l/2):
            if l%(i+1)==0 :
                flag = True
                for j in range(0,l)[::i+1]:
                    if s[j:j+i+1]!=s[0:i+1]:
                        flag = False
                        break
                if (flag): return True
        return False
        
 #OR
 class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in (s*2)[1:-1]
