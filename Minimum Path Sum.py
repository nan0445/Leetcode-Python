class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        s = [[0]*n]*m
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    s[i][j] = grid[i][j]
                elif i==0 and j>0:
                    s[i][j] = s[i][j-1] + grid[i][j]
                elif i>0 and j==0:
                    s[i][j] = s[i-1][j] + grid[i][j]
                else:
                    s[i][j] = min(s[i-1][j], s[i][j-1]) + grid[i][j]
        return s[m-1][n-1]
