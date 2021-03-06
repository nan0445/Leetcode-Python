class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        dp = [[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]
        for i in range(len(dungeon))[::-1]:
            for j in range(len(dungeon[0]))[::-1]:
                if i==len(dungeon)-1 and j==len(dungeon[0])-1:
                    dp[i][j] = max(1, 1-dungeon[i][j])
                elif i==len(dungeon)-1:
                    dp[i][j] = max(dp[i][j+1] - dungeon[i][j], 1)
                elif j==len(dungeon[0])-1:
                    dp[i][j] = max(dp[i+1][j] - dungeon[i][j], 1)
                else:
                    dp[i][j] = min(max(dp[i][j+1] - dungeon[i][j], 1), max(dp[i+1][j] - dungeon[i][j], 1))
                
        return dp[0][0]
