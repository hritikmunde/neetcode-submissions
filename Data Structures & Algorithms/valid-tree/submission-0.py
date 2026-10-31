class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = {0}
        stack = [0]

        while stack:
            node = stack.pop()
            for nxt in graph[node]:
                if nxt not in visited:
                    visited.add(nxt)
                    stack.append(nxt)
        return len(visited) == n