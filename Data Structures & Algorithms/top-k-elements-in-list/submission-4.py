class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for n in nums:
            if n not in h:
                h[n]=1
            else:
                h[n] += 1
        mh = []
        import heapq
        for (num, cnt) in h.items():
            if len(mh) < k:
                heapq.heappush(mh, (cnt, num))
            else:
                if cnt > mh[0][0]:
                    # heapq.heappop(mh)
                    # heapq.heappush(mh, (cnt, num))
                    heapq.heapreplace(mh, (cnt, num))
        
        return [x[1] for x in mh]