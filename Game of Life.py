class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def count(i,j):
            s = 0
            for inx, [ind, jnd] in enumerate([[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]):
                if i+ind>=0 and j+jnd>=0 and i+ind<len(board) and j+jnd<len(board[0]):
                    if board[i+ind][j+jnd] == 1 or board[i+ind][j+jnd] == 3: s += 1
            return s
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                n = count(i,j)
                if board[i][j] == 1:
                    if n<=1 or n>3: board[i][j] += 2
                else:
                    if n==3: board[i][j] += 2
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 3: board[i][j] = 0
                elif board[i][j] == 2: board[i][j] = 1
