class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        res = 0
        h = len(matrix)
        if h==0: return 0
        w = len(matrix[0])
        for i in range(h):
            for j in range(w):
                if res>=(h-i)*(w-j): break
                l = w-j
                for p in range(i,h):
                    if matrix[p][j]=='0': break
                    for q in range(j,w):
                        if matrix[p][q]=='0': 
                            l = q-j
                            res = max(res,(p-i+1)*l)
                            break
                        if p>i and q-j+1>=l: 
                            res = max(res,(p-i+1)*l)
                            break
                    else: res = max(res,(p-i+1)*l)
                        
        return res
                     
########## OR use the same strategy of the maximal area in last quesiont###################

class Solution:
    def maximalRectangle(self, matrix):
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
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(n+1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                stack.append(i)
        return ans
