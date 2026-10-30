class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        from collections import defaultdict
        adjL = defaultdict(list)
        for i, j, c in flights:
            adjL[i].append((j,c))
        dp = {} # dp[(i,)]

        def dfs(node, i):
            if node == dst:
                return 0
            if i == k + 1:
                return float('inf')
            if (node, i) in dp:
                return dp[node, i]
            else:
                dp[(node, i)] = min([c + dfs(x, i+1) for x, c in adjL[node]], default=float('inf'))
            return dp[(node, i)]
        
        res = dfs(src, 0)
        return res if res < float('inf') else -1