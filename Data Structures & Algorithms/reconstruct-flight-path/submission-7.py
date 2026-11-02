from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)

        route = []
        def dfs(node):
            while adj[node]:
                dfs(adj[node].pop())
            route.append(node)

        dfs('JFK')
        return route[::-1]