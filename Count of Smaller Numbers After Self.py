class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        sort = []
        for n in nums[::-1]:                              
            bisect.insort(sort, n)
            res.append(bisect.bisect_left(sort, n))
        return res[::-1]
