class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pac = set([(0,y) for y in range(0, cols)] + [(x,0) for x in range(0, rows)])
        atl = set([(rows-1, y) for y in range(0, cols)] + [(x, cols-1) for x in range(0, rows)])

        directions = [(0,-1), (0,1), (-1,0), (1,0)]
        
        # fill pacific cells
        stack = list(pac)
        while stack:
            new_level = []
            for _ in range(len(stack)):
                x, y = stack.pop()
                for dx, dy in directions:
                    newx, newy = x+dx, y+dy
                    if newx >= 0 and newy >=0 and newx < rows and newy < cols and (newx, newy) not in pac:
                        if heights[newx][newy] >= heights[x][y]:
                            pac.add((newx, newy))
                            new_level.append((newx, newy))
            
            stack = new_level
        
        # fill atlantic cells
        stack = list(atl)
        while stack:
            new_level = []
            for _ in range(len(stack)):
                x, y = stack.pop()
                for dx, dy in directions:
                    newx, newy = x+dx, y+dy
                    if newx >= 0 and newy >=0 and newx < rows and newy < cols and (newx, newy) not in atl:
                        if heights[newx][newy] >= heights[x][y]:
                            atl.add((newx, newy))
                            new_level.append((newx, newy))
            
            stack = new_level
        
        return list(atl.intersection(pac))
