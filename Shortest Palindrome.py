class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ""
        for i in range(len(s))[::-1]:
            if s[:i+1] == s[:i+1][::-1]:
                return s[i+1:][::-1] + s
##########################################
############ Advanced function ####################
class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = s[::-1]
        for i in range(len(r)):
            if s.startswith(r[i:]):
                return r[:i] + s
        return s
        
##########################################
##########################################
class Solution:
    def shortestPalindrome(self, s):
        
        def prefixFunction(s):
            p = [0] * len(s)
            for i in range(1, len(s)):
                j = p[i - 1]
                while s[i] != s[j] and j:
                    j = p[j - 1]
                p[i] = j + (1 if s[j] == s[i] else 0)
            return p
        if len(s) < 1: return s
        p = prefixFunction(s + '#' + s[::-1])
        return s[p[-1]:][::-1] + s
