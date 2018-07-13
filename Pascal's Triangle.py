class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            res.append([0 for _ in range(i+1)])
            for j in range(i+1):
                if j==0: res[i][j] = 1
                elif j==i: res[i][j] = 1
                else:
                    res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res
        
