class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict
        adjL = defaultdict(list)
        for i, j in edges:
            adjL[i].append(j)
            adjL[j].append(i)

        visited = set()
        def dfs(i, par):
            if i in visited:
                return False
            
            visited.add(i)
            for ch in adjL[i]:
                if ch == par:
                    continue
                if not dfs(ch, i): return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n