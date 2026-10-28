class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        area = 0

        def dfs(row, col):
            if row >= rows or row < 0 or col >= cols or col < 0:
                return 0
            if (row, col) in visited or grid[row][col] == 0:
                return 0
            visited.add((row, col))
            return (1 + dfs(row - 1, col) +
            dfs(row + 1, col) +
            dfs(row, col - 1) +
            dfs(row, col + 1))
            
        
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == 1:
                    area = max(area, dfs(row, col))
        return area