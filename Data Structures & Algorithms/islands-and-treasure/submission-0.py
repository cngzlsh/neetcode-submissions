class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        stack = []
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 0:
                    stack.append((x,y))
        
        # multi-source BFS
        visited = set(stack)
        step = 0
        while stack:
            step += 1
            new_level = []
            for _ in range(len(stack)):
                x, y = stack.pop()
                
                for dx, dy in directions:
                    if x + dx >= 0 and y + dy >= 0 and x + dx < m and y + dy < n and grid[x+dx][y+dy] > 0 and (x+dx, y+dy) not in visited:
                        grid[x+dx][y+dy] = step
                        visited.add((x+dx, y+dy))
                        new_level.append((x+dx, y+dy))
            stack = new_level

