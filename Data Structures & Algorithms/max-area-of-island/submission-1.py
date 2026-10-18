class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(x, y):
            # returns the area of the island part reachable from (x, y); 0 if invalid or water
            if not (0 <= x < rows and 0 <= y < cols) or grid[x][y] == 0:
                return 0
            grid[x][y] = 0                      # sink: doubles as the visited marker
            return 1 + dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1)

        best = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    best = max(best, dfs(i, j))
        return best