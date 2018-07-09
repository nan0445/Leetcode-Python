class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        l,t = {},{}
        temp = []
        def helper(i,n):
            if i==n:
                x = []
                for p in t:
                    x.append(t[p])
                temp.append(x[:])
                return
            for j in range(n):
                if j in l: continue
                for q in t:
                    if abs(i-t[q][0])==abs(j-t[q][1]):
                        break
                else:
                    l[j] = 1
                    t[i] = (i,j)
                    helper(i+1,n)
                    del l[j]
                    del t[i]
        helper(0,n)
        res = []
        for v in temp:
            m = [['.' for _ in range(n)] for _ in range(n)]
            for i in v:
                m[i[0]][i[1]] = 'Q'
            for q in range(n): m[q] = ''.join(m[q])
            res.append(m[:])
        return res
