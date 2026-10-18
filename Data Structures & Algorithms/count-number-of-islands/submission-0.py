class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows, cols = len(grid), len(grid[0])

        def dfs(xy):
            x, y = xy
            if grid[x][y] == '0': 
                return
            else:
                grid[x][y] = '0'
                for dx, dy in directions:
                    if x + dx >= 0 and x + dx < rows and y + dy >= 0 and y + dy < cols:
                        dfs((x + dx, y+dy))
        
        islands = 0
        for m in range(rows):
            for n in range(cols):
                if grid[m][n] == '1':
                    islands += 1
                    dfs((m,n))
        
        return islands