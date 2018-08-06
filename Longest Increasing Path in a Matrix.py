class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.res = 0
        self.dic = {}
        def helper(x, y, pre):
            if x<0 or y<0 or x>=len(matrix) or y>=len(matrix[0]) or matrix[x][y]<=pre: return 0
            if (x,y) in self.dic: return self.dic[(x,y)]
            path = 1 + max(helper(x-1,y, matrix[x][y]), helper(x+1, y, matrix[x][y]), helper(x, y-1, matrix[x][y]), helper(x, y+1, matrix[x][y]))
            self.dic[(x, y)] = path
            self.res = max(self.res, path)
            return path
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                helper(i,j,-2**31)
        return self.res
            
