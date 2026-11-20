class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        orig2clone = {}

        def dfs(orig):
            if orig in orig2clone:
                return orig2clone[orig]
            clone = Node(orig.val)
            orig2clone[orig] = clone          # register BEFORE recursing
            clone.neighbors = [dfs(nb) for nb in orig.neighbors]
            return clone

        return dfs(node) if node else None