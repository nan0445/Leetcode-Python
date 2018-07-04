class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        l,r = 0, len(matrix)-1
        if len(matrix)==0: return False
        if len(matrix[0])==0: return False
        while l<r:
            mid = (l+r)//2
            if matrix[mid][0]>target:
                r = mid
            elif matrix[mid][0]<target:
                l = mid + 1
            else: return True
        if matrix[l][0]>target:
            if l==0: return False
            l -= 1
        i = l
        l = 0
        r = len(matrix[0])-1
        while l<r:
            mid = (l+r)//2
            if matrix[i][mid]>target:
                r = mid
            elif matrix[i][mid]<target:
                l = mid + 1
            else: return True
        if matrix[i][l]==target: return True
        return False
