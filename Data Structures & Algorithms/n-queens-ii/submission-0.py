class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        cols = set()
        fdiag = set()
        bdiag = set()

        def backtrack(row):
            if row == n:
                nonlocal res
                res += 1
            
            for col in range(n):
                if (col not in cols) and (col + row) not in fdiag and (col - row) not in bdiag:
                    cols.add(col)
                    fdiag.add(col+row)
                    bdiag.add(col-row)

                    backtrack(row + 1)

                    cols.remove(col)
                    fdiag.remove(col+row)
                    bdiag.remove(col-row)
            return
        
        backtrack(0)
        return res