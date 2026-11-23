class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        # find treasure, then multi source bfs
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))
        
        step = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = step
                
                for dr, dc in ([-1,0],[1,0],[0,-1],[0,1]):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] > 0:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            step += 1