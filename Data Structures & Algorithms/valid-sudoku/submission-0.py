class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {(i, j): True for i in range(0,9) for j in range(1, 10)} # row [i, num j]
        cols = {(i, j): True for i in range(0,9) for j in range(1, 10)}

        for i in range(3):
            for j in range(3):
                block = {i:True for i in range(1,10)}
                for r in range(3):
                    for c in range(3):
                        x, y = 3 * i + c, 3 * j + r
                        if board[x][y] == '.': continue
                        if not rows[(x, int(board[x][y]))]: return False
                        if not cols[(y, int(board[x][y]))]: return False
                        rows[(x, int(board[x][y]))] = False
                        cols[(y, int(board[x][y]))] = False
                        if not block[int(board[x][y])]: return False
                        block[int(board[x][y])] = False
        
        return True
