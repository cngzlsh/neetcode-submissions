class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import deque, Counter
        import heapq
        q = deque()
        h = [-cnt for cnt in Counter(tasks).values()]
        heapq.heapify(h)
        t = 0
        while h or q:
            t += 1
            if h:
                cnt = heapq.heappop(h) + 1
                if cnt:
                    q.append((t+n, cnt))
            if q and q[0][0] == t:
                heapq.heappush(h, q.popleft()[1])
        return t