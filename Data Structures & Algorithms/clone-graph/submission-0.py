"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = {}
        def dfs(node):
            if node in hashmap:
                return hashmap[node]
            graphNode = Node(node.val)
            hashmap[node] = graphNode
            for neighbor in node.neighbors:
                graphNode.neighbors.append(dfs(neighbor))
            return graphNode
        return dfs(node) if node else None
           