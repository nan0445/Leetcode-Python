class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res, S, L = 0, [], []
        for i in words:
            S.append(set(list(i)))
            L.append(len(i))
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not S[i] & S[j]:
                    res = max(res, L[i] * L[j])
        return res
