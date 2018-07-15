class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        h = len(board)
        if h==0: return
        w = len(board[0])
        
        def helper(p,q,board):
            if p<0 or q<0 or p>len(board)-1 or q>len(board[0])-1 or board[p][q]!='O': return
            board[p][q]='T'
            helper(p-1,q,board)
            helper(p,q-1,board)
            helper(p+1,q,board)
            helper(p,q+1,board)
            
        
        for i in [0,h-1]:
            for j in range(w):
                if board[i][j]=='O':
                    helper(i,j,board)
        for j in [0,w-1]:
            for i in range(h):
                if board[i][j]=='O':
                    helper(i,j,board)
        for i in range(h):
            for j in range(w):
                if board[i][j] == 'O': board[i][j] = 'X'
        for i in range(h):
            for j in range(w):
                if board[i][j] == 'T': board[i][j] = 'O'            
