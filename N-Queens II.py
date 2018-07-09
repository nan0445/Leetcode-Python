class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,t = {},{}
        self.ans = 0
        def helper(i,n):
            if i==n:
                self.ans += 1
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
        return self.ans
