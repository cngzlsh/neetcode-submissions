class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(0,-1), (0,1), (-1,0), (1,0)]
        visited = set()

        def region_is_enclosed(r, c):
            # iterative DFS; returns (enclosed, cells)
            stack = [(r, c)]
            visited.add((r, c))
            cells = []
            enclosed = True
            while stack:
                x, y = stack.pop()
                cells.append((x, y))
                if x in (0, rows - 1) or y in (0, cols - 1):
                    enclosed = False              # touches border; keep going, don't exit early
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < rows and 0 <= ny < cols
                            and board[nx][ny] == 'O' and (nx, ny) not in visited):
                        visited.add((nx, ny))
                        stack.append((nx, ny))
            return enclosed, cells

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in visited:
                    enclosed, cells = region_is_enclosed(r, c)
                    if enclosed:
                        for x, y in cells:
                            board[x][y] = 'X'