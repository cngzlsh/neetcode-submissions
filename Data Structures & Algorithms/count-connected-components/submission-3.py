class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = {i:i for i in range(n)} #child -> parent
        rank = {i:1 for i in range(n)}

        def find(a):
            p = par[a]
            while par[a]!=a:
                par[a] = par[par[a]]
                a = par[a]
            return a
        
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return False
            if rank[pa] > rank[pb]:
                par[pb] = pa
                rank[pa] += rank[pb]
            else:
                par[pa] = pb
                rank[pb] += rank[pa]
            return True

        components = n
        for a, b in edges:
            if union(a, b):
                components -= 1
        return components
