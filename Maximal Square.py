class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0
        for row in matrix:
            stack = [-1]
            for i in range(n+1):
                if i<n:
                    height[i] = height[i] + 1 if row[i] == '1' else 0
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, min(h, w)**2)
                stack.append(i)
               
        return ans
