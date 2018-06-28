class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        res = []
        for i in strs:
            temp = ''.join(sorted(i))
            if temp in dic:
                dic[temp].append(i)
            else:
                dic[temp] = [i]
        for i in dic:
            res.append(dic[i])
        return res
