class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        import heapq
        n = len(grid)
        directions = [(0,1),(1,0), (0,-1),(-1,0)]
        time = 0
        minHeap = [(grid[0][0], 0,0)]
        heapq.heapify(minHeap)
        visited = set()
        visited.add((0,0))
        while True:
            t, r, c = heapq.heappop(minHeap)
            visited.add((r, c))
            time = max(t, time)
            if r == n-1 and c == n-1:
                break

            for dx, dy in directions:
                nx, ny = r + dx, c + dy
                if (nx, ny) not in visited and 0 <= nx < n and 0 <= ny < n:
                    heapq.heappush(minHeap, (grid[nx][ny], nx, ny))

        return time