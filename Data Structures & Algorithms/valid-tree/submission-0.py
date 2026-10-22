class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adjl = {i: [] for i in range(n)}
        for a, b in edges:
            adjl[a].append(b)
            adjl[b].append(a)

        seen = {0}
        stack = [0]
        while stack:
            node = stack.pop()
            for nb in adjl[node]:
                if nb not in seen:
                    seen.add(nb)
                    stack.append(nb)
        return len(seen) == n