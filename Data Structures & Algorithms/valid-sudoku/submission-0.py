class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # size 9 x 9
        # thay vì tạo array lưu index theo từng số -> tạo array r,c,square để stock các số và kiểm tra luôn :D
        r = arr = [[] for _ in range(9)]
        c = arr = [[] for _ in range(9)]
        square = [[[] for _ in range(3)] for _ in range(3)]
        for i in range (9):
            for j in range(9):
                if board[i][j].isnumeric():
                    if board[i][j] in r[i] or board[i][j] in c[j] or board[i][j] in square[i//3][j//3]:
                        return False
                    r[i].append(board[i][j])
                    c[j].append(board[i][j])
                    square[i//3][j//3].append(board[i][j])
        
        return True