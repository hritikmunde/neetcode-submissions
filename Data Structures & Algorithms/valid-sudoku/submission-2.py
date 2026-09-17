class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                s = board[i][j]
                if s == ".":
                    continue
                box_index = (i // 3) * 3 + (j // 3)
                if s in rows[i] or s in cols[j] or s in boxes[box_index]:
                    return False
                rows[i].add(s)
                cols[j].add(s)
                boxes[box_index].add(s)
        return True