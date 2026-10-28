class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        count = 0

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            if (row, col) in visited or grid[row][col] == "0":
                return
            visited.add((row, col))
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == "1":
                    count += 1
                    dfs(row, col)
        return count