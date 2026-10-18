class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        fresh = 0
        stack = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    stack.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        
        # multi-source BFS
        minutes = 0
        if fresh == 0: return minutes
        while stack:
            minutes += 1
            newly_rotten = []
            for _ in range(len(stack)):
                x, y = stack.pop()
                for dx, dy in directions:
                    if x + dx >= 0 and y + dy >= 0 and x + dx < rows and y + dy < cols:
                        if grid[x+dx][y+dy] == 1:
                            grid[x+dx][y+dy] = 2
                            newly_rotten.append((x+dx, y+dy))
                            fresh -= 1
            stack = newly_rotten
        
        if fresh == 0: 
            return minutes - 1
        else:
            return -1