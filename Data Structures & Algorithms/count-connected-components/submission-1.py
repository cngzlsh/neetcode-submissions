class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        cluster = [i for i in range(n)]
        pa = [i for i in range(n)]
        from collections import defaultdict
        adjL = defaultdict(list)
        for i, j in edges:
            adjL[i].append(j)
            adjL[j].append(i)

        def find(n):
            # return a node's parent
            while pa[n] != n:
                pa[n] = pa[pa[n]]
                n = pa[n]
            return n
        
        def union(n1, n2):
            p1 = find(n1)
            pa[find(n2)] = p1
        
        for i in range(n):
            for neig in adjL[i]:
                union(i,neig)
        
        return len({find(i) for i in range(n)})

