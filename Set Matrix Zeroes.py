class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    for p in range(n):
                        if p<=j: matrix[i][p]=0
                        elif p>j and matrix[i][p]!=0: matrix[i][p] = None
                    for q in range(m):
                        if q<=i: matrix[q][j]=0
                        elif q>i and matrix[q][j]!=0: matrix[q][j] = None
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==None:
                    matrix[i][j] = 0
            
