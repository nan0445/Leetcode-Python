class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t): return False
        dic = {}
        c = set()
        for i in range(len(s)):
            if s[i] not in dic and t[i] not in c:
                dic[s[i]] = t[i]
                c.add(t[i])
            elif s[i] in dic:
                if dic[s[i]] != t[i]: return False
            elif s[i] not in dic and t[i] in c: return False
        return True
