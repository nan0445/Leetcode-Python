class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations: return 0
        citations.sort(reverse = True)
        for i, v in enumerate(citations):
            if i + 1 > v: return i
        return i + 1
