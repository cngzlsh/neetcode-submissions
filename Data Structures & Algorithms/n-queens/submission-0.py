class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # backtracking on row
        board = [["."] * n for _ in range(n)]
        res = []
        cols, posdiag, negdiag = set(), set(), set()

        def backtrack(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or r + c in posdiag or r - c in negdiag:
                    continue
                
                board[r][c] = 'Q'
                cols.add(c)
                posdiag.add(r + c)
                negdiag.add(r - c)
                backtrack(r+1)

                # undo
                cols.remove(c)
                posdiag.remove(r + c)
                negdiag.remove(r - c)
                board[r][c] = '.'
        
        backtrack(0)
        return res
        
        