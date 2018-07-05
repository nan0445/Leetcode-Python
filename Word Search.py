class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        def helper(p,q,t,board,word):
            if p<0 or p>=len(board) or q<0 or q>=len(board[0]) or board[p][q] != word[t]: return False
            board[p][q] = '#'
            if t == len(word)-1: return True
            a1 = helper(p-1,q,t+1,board,word) or helper(p,q-1,t+1,board,word) or helper(p+1,q,t+1,board,word) or helper(p,q+1,t+1,board,word)
            board[p][q] = word[t]
            return a1
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if helper(i,j,0,board,word): return True
                    
        return False
    
        
            
