class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(row, col, char_index):
            if char_index == len(word):
                return True
            if row >= rows or row < 0 or col >= cols or col < 0 or board[row][col] != word[char_index] or (row, col) in visited:
                return False

            visited.add((row, col))
            res = (dfs(row + 1, col, char_index + 1) or 
                   dfs(row - 1, col, char_index + 1) or 
                   dfs(row, col + 1, char_index + 1) or 
                   dfs(row, col - 1, char_index + 1))
            visited.remove((row, col))
            return res
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False
            
