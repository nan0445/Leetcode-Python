class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        head = {}
        end = "end"
        for i in words:
            root = head
            for c in i:
                if c not in root:
                    root[c] = {}
                    
                root = root[c]
            root[end] = True
        
        res = set()
        temp = []
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        
        def helper(x,y,r):
            if x<0 or y<0 or x>=len(board) or y>=len(board[0]) or board[x][y] not in r or visited[x][y]: return
            visited[x][y] = True
            temp.append(board[x][y])
            if 'end' in r[board[x][y]]: 
                res.add(''.join(temp[:]))
                
            helper(x-1, y, r[board[x][y]])
            helper(x+1, y, r[board[x][y]])
            helper(x, y-1, r[board[x][y]])
            helper(x, y+1, r[board[x][y]])
            visited[x][y] = False
            temp.pop()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in head:
                    helper(i,j,head)
        return list(res)
