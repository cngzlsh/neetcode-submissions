class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacifics = set()
        atlantics = set()

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        def pacific_dfs(r, c):
            if (r, c) in pacifics:
                return
            pacifics.add((r, c))
            for dx, dy in directions:
                nx, ny = r + dx, c + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in pacifics and heights[nx][ny] >= heights[r][c]:
                    
                    pacific_dfs(nx, ny)
        
        def atlantic_dfs(r, c):
            if (r, c) in atlantics:
                return
            
            atlantics.add((r, c))
            for dx, dy in directions:
                nx, ny = r + dx, c + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in atlantics and heights[nx][ny] >= heights[r][c]:
                    
                    atlantic_dfs(nx, ny)
        
        for (pr, pc) in [(r,0) for r in range(rows)] + [(0, c) for c in range(cols)]:
            pacific_dfs(pr, pc)
        
        for (ar, ac) in [(r,cols-1) for r in range(rows)] + [(rows-1, c) for c in range(cols)]:
            atlantic_dfs(ar, ac)
        
        return [list(x) for x in pacifics.intersection(atlantics)]
        
