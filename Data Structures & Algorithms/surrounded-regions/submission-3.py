class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(0,-1), (0,1), (-1,0), (1,0)]
        visited = set()

        def is_enclosed(r, c):
            # pass 1: read-only; visits the whole region, never exits early
            stack = [(r, c)]
            visited.add((r, c))
            enclosed = True
            while stack:
                x, y = stack.pop()
                if x in (0, rows - 1) or y in (0, cols - 1):
                    enclosed = False
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < rows and 0 <= ny < cols
                            and board[nx][ny] == 'O' and (nx, ny) not in visited):
                        visited.add((nx, ny))
                        stack.append((nx, ny))
            return enclosed

        def fill(r, c):
            # pass 2: flips the region; the 'X' is the visited marker
            stack = [(r, c)]
            board[r][c] = 'X'
            while stack:
                x, y = stack.pop()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == 'O':
                        board[nx][ny] = 'X'
                        stack.append((nx, ny))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in visited and is_enclosed(r, c):
                    fill(r, c)