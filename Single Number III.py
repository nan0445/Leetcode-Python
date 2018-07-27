class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r = 0
        for i in nums:
            r ^= i
        x = r & ~(r - 1)
        n1, n2 = 0, 0
        for i in nums:
            if x & i: n1 ^= i
            else: n2 ^= i
        return [n1, n2]
        
