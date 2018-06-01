class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if len(strs)==0: return ""
        for i in range(0,len(strs[0])):
            flag = True
            for j in range(1,len(strs)):
                if i>=len(strs[j]):
                    return res
                if strs[j][i]!=strs[0][i]:
                    flag = False
                    return res
            if (flag):
                res += strs[0][i]
            
        return res
