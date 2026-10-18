class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows, cols = len(grid), len(grid[0])

        def dfs(xy):
            nonlocal island_area
            x, y = xy
            if grid[x][y] == 0: 
                return 
            else:
                grid[x][y] = 0
                island_area += 1
                for dx, dy in directions:
                    if x + dx >= 0 and x + dx < rows and y + dy >= 0 and y + dy < cols:
                        dfs((x+dx, y+dy))

        max_area = 0
        for m in range(rows):
            for n in range(cols):
                if grid[m][n] == 1:
                    island_area = 0
                    dfs((m,n))
                    max_area = max(max_area, island_area)
        
        return max_area