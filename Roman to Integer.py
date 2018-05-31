class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,"XC":90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
        i=0
        res=0
        while i<len(s):
            i_next = i+2
            if s[i:i_next] in lookup:
                res+=lookup[s[i:i_next]]
                i+=2
            else:
                res+=lookup[s[i]]
                i+=1
        return res
