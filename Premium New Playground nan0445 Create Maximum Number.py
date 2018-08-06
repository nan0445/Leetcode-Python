class Solution:
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def preN(nums, n):
            res = []
            left = len(nums) - n
            for i in nums:
                while res and res[-1]<i and left>0:
                    res.pop()
                    left -= 1
                res.append(i)
            return res[:n]
        
        def merge(a, b):
            return [max(a, b).pop(0) for _ in a+b]
        
        ans = []
        for i in range(k+1):
            if i<=len(nums1) and k-i<=len(nums2):
                ans.append(merge(preN(nums1, i), preN(nums2, k-i)))
        return max(ans)
