class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i,j = m-1,n-1
        for ind in range(m+n-1,-1,-1):
            if j<0: break
            if i>=0 and nums2[j]>=nums1[i]: 
                nums1[ind] = nums2[j]
                j -= 1
            elif i>=0 and nums2[j]<nums1[i]:
                nums1[ind] = nums1[i]
                i -= 1
            elif i<0:
                nums1[ind] = nums2[j]
                j -= 1
        
