class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix)==0: return []
        m = len(matrix)
        n = len(matrix[0])
        count = 0
        ans = []
        i = 0
        c = 0
        while c<m*n:
            if count%4==0:
                ans += matrix[i]
                c += len(matrix[i])
                matrix[i] = []
                
            elif count%4==1:
                while i<m-count//4-1:
                    i += 1
                    c += 1
                    ans.append(matrix[i].pop())
            elif count%4==2:
                ans += matrix[i][::-1]
                c += len(matrix[i])
                matrix[i] = []
            else:
                while i>count//4+1:
                    i -= 1
                    c += 1
                    ans.append(matrix[i].pop(0))
            count += 1
        return ans
