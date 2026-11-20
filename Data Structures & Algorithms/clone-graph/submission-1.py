"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node
        orig2clone = {}

        clone = Node(val = node.val)
        orig2clone[node] = clone

        def dfs(orig):
            for ch in orig.neighbors:
                if ch in orig2clone:
                   orig2clone[orig].neighbors.append(orig2clone[ch])
                else:
                    newNode = Node(val = ch.val)
                    orig2clone[ch] = newNode
                    orig2clone[orig].neighbors.append(orig2clone[ch])
                    dfs(ch)
        
        dfs(node)
        
        return clone