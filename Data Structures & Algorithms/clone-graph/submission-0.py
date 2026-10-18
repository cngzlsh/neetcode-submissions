"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        orig2clone = {}
        
        def dfs(n):
            # n is original node
            if not n:
                return n

            if n not in orig2clone: 
                newnode = Node(n.val)
                orig2clone[n] = newnode
            else:
                return orig2clone[n]

            for neig in n.neighbors:
                newnode.neighbors.append(dfs(neig))

            return newnode
        
        return dfs(node)