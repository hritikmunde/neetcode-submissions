class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        maxArea = 0

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))
            res = 1

            while q:
                row, col = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 0 or (nr, nc) in visited):
                        continue
                    q.append((nr, nc))
                    visited.add((nr, nc))
                    res += 1
            return res
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(maxArea, bfs(r, c))
        return maxArea