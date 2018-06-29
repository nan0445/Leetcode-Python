class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        r,l,t = collections.defaultdict(set),collections.defaultdict(set),collections.defaultdict(set)
        #visit = collections.deque([])
        visit = []
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    r[i].add(board[i][j])
                    l[j].add(board[i][j])
                    t[(i//3,j//3)].add(board[i][j])
                else:
                    visit.append((i,j))
                    
        def helper():
            if not visit: return True
            p,q = visit[0]
            for v in ['1','2','3','4','5','6','7','8','9']:
                if v not in r[p] and v not in l[q] and v not in t[(p//3,q//3)]:
                    board[p][q] = v
                    #visit.popleft()
                    visit.pop(0)
                    r[p].add(v)
                    l[q].add(v)
                    t[(p//3,q//3)].add(v)
                    if helper(): return True
                    else:
                        board[p][q] = '.'
                        #visit.appendleft((p,q))
                        visit.insert(0,(p,q))
                        r[p].discard(v)
                        l[q].discard(v)
                        t[(p//3,q//3)].discard(v)
            return False
        
        helper()
                    
