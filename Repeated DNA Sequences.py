class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = {}
        res = []
        for i in range(len(s)-9):
            if s[i:i+10] not in dic:
                dic[s[i:i+10]] = 1
            else: 
                if dic[s[i:i+10]] == 1:
                    res.append(s[i:i+10])
                dic[s[i:i+10]] += 1
        return res
