class Solution:
    def isValidSudoku(self,board):
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    current_num = board[r][c]
                    if current_num in rows[r] or current_num in cols[c] or current_num in boxes[(r//3, c//3)]:
                        return False
                    rows[r].add(current_num)
                    cols[c].add(current_num)
                    boxes[(r//3, c//3)].add(current_num)
        return True