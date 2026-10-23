class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dijkstra's algorithm
        from collections import defaultdict
        import heapq
        
        adjL = defaultdict(list)
        for u, v, w in times:
            adjL[u].append((v, w))
        
        minHeap = [(0,k)]
        total = 0
        visited = set()
        while minHeap:
            t1, v = heapq.heappop(minHeap)
            if v in visited:
                continue
            visited.add(v)
            total = max(total, t1)

            for neig, t2 in adjL[v]:
                if neig not in visited:
                    heapq.heappush(minHeap, (t1 + t2, neig))
        
        return total if len(visited) == n else -1
