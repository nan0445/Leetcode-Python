class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        dic = {}
        l = len(board)
        for i in range(l):
            dic = {}
            for j in range(l):
                if board[i][j] in dic: return False
                elif board[i][j]!=".": dic[board[i][j]] = 1
        for i in range(l):
            dic = {}
            for j in range(l):
                if board[j][i] in dic: return False
                elif board[j][i]!=".": dic[board[j][i]] = 1
        for i in [1,4,7]:
            for j in [1,4,7]:
                dic = {}
                for p in [-1,0,1]:
                    for q in [-1,0,1]:
                        if board[i+p][j+q] in dic: return False
                        elif board[i+p][j+q]!=".": dic[board[i+p][j+q]] = 1
        return True
