class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        w = len(matrix) - 1
        p,q = 0,w
        while p<q:
            for j in range(p,q):
                temp = matrix[p][j]
                matrix[p][j] = matrix[w-j][p]
                matrix[w-j][p] = matrix[w-p][w-j]
                matrix[w-p][w-j] = matrix[j][w-p]
                matrix[j][w-p] = temp
                print(temp)
            p += 1
            q -= 1
        
                
