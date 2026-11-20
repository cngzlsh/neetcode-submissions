class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, fdiag, bdiag = set(), set(), set()
        res = []
        def backtrack(row, path):
            if row == n:
                res.append(path[:])
                return
            
            for col in range(n):
                # try and place Q on grid[row][col]
                if col not in cols and (row - col) not in fdiag and (row + col) not in bdiag:
                    cols.add(col)
                    fdiag.add(row - col)
                    bdiag.add(row + col)
                    
                    tmp = '.' * (col) + 'Q' + '.' * (n - col - 1)
                    path.append(tmp)
                    backtrack(row+1, path)
                    path.pop()
                    cols.remove(col)
                    fdiag.remove(row - col)
                    bdiag.remove(row + col)
        
        backtrack(0,[])
        return res
