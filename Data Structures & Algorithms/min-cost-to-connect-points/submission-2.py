class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        import heapq
        n = len(points)
        

        curr_x, curr_y = points[0]
        visited = set()
        visited.add((curr_x, curr_y))
        totalCost = 0

        minHeap = []
        heapq.heapify(minHeap)

        while len(visited)!= n:
            for x, y in points:
                if (x,y) not in visited:
                    heapq.heappush(minHeap, (abs(x - curr_x) + abs(y - curr_y), (x, y)))
            
            for _ in range(len(minHeap)):
                cost, (curr_x, curr_y) = heapq.heappop(minHeap)
                if (curr_x, curr_y) not in visited:
                    break
            totalCost += cost

            visited.add((curr_x, curr_y))
            

        return totalCost