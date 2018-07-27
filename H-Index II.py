class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations: return 0
        n = len(citations)
        l, r = 0, n - 1
        res = 0
        while l<r:
            mid = (l + r) // 2
            if citations[mid] > n - mid - 1: r = mid
            elif citations[mid] < n - mid - 1: l = mid + 1
            else: 
                res = max(res, n - mid - 1)
                r = mid
        #print (l, r)
        return max(res, n - l - 1 if citations[l] <= n - l - 1  else n - l)
