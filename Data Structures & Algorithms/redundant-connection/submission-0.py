class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # this is a union find problem...

        pa = [i for i in range(len(edges)+1)]
        def find(i):
            while pa[i] != i:
                pa[i] = pa[pa[i]]
                i = pa[i]
            return i
        def union(i, j):
            pi = find(i)
            pj = find(j)
            if pi == pj: return False

            pa[pj] = pi
            return True
        
        for i, j in edges:
            if not union(i, j): return [i,j]