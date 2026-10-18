class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(x, y, k):
            if k == len(word):
                return True
            if not (0 <= x < rows and 0 <= y < cols) or board[x][y] != word[k]:
                return False
            tmp = board[x][y]
            board[x][y] = "#"                      # mark as used
            ok = (dfs(x+1, y, k+1) or dfs(x-1, y, k+1) or
                  dfs(x, y+1, k+1) or dfs(x, y-1, k+1))
            board[x][y] = tmp                      # undo
            return ok

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False