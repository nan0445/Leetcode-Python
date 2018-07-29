class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s=str.split()
        dic = {}
        word = set()
        if len(s) != len(pattern): return False
        for i in range(len(pattern)):
            if pattern[i] not in dic:
                if s[i] not in word: 
                    dic[pattern[i]] = s[i]
                    word.add(s[i])
                else: return False
            else:
                if dic[pattern[i]] != s[i]:
                    return False
        return True
        
