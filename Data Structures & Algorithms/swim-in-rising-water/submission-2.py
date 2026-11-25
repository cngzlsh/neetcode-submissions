class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        import heapq
        n = len(grid)
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        minHeap = [[grid[0][0],(0,0)]]
        heapq.heapify(minHeap)
        t = 0
        visited = set((0,0))

        # BFS on minHeap:
        while True:
            while minHeap and minHeap[0][0] <= t:
                _, (x,y) = heapq.heappop(minHeap)
                
                if x == n-1 and y == n-1: 
                    return t
                
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                        heapq.heappush(minHeap, [grid[nx][ny], (nx, ny)])
                        visited.add((nx, ny))

            t += 1