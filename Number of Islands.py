class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        count = 0
        
        def helper(i,j,grid):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!='1': return
            grid[i][j] = 'X'
            helper(i-1,j,grid)
            helper(i+1,j,grid)
            helper(i,j-1,grid)
            helper(i,j+1,grid)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    helper(i,j,grid)
        return count
 
