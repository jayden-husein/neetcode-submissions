class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        sq = defaultdict(set)

        for r in range(0, len(board)):
            for c in range(0, len(board)):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in row[r] or 
                    board[r][c] in col[c] or 
                    board[r][c] in sq[(r // 3, c // 3)]):
                    return False
                
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                sq[(r // 3, c //3)].add(board[r][c])

        return True
