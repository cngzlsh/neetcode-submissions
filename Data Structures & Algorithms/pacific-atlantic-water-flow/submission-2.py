class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacifics = set()
        atlantics = set()

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        def dfs(r, c, seen):
            if (r, c) in seen:
                return
            seen.add((r, c))
            for dx, dy in directions:
                nx, ny = r + dx, c + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in seen and heights[nx][ny] >= heights[r][c]:
                    dfs(nx, ny, seen)
        
        
        for (pr, pc) in [(r,0) for r in range(rows)] + [(0, c) for c in range(cols)]:
            dfs(pr, pc, pacifics)
        
        for (ar, ac) in [(r,cols-1) for r in range(rows)] + [(rows-1, c) for c in range(cols)]:
            dfs(ar, ac, atlantics)
        
        return [list(x) for x in pacifics.intersection(atlantics)]
        
