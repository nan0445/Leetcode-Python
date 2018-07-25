class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        if target < matrix[0][0] or target > matrix[-1][-1]: return False
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target: return True
            elif matrix[row][col] < target: row += 1
            else: col -= 1
        return False
        
            
