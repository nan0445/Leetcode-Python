class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        M = (collections.Counter(nums1) & collections.Counter(nums2))
        return [i for i in M for _ in range(M[i])]
