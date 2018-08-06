class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        C = collections.Counter(s)
        B = collections.defaultdict(bool)
        res = []
        for cha in s:
            C[cha] -= 1
            if B[cha]: continue
            while res and C[res[-1]]>0 and cha < res[-1]:
                B[res.pop()] = False
            B[cha] = True
            res.append(cha)
        return ''.join(res)
