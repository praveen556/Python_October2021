class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        results = []
        def is_sudoku(str):
            for i in range(1,10):
                for j in range(i,10):
                    if str[i][i]!=str[i][j]:
                        return True
                    else:
                        return False
        def helper(str, i, k):
            if is_sudoku(str):
                return str
            else:
                if str[i][k].isdigit:
                    helper(str,i, k+1)
                else:
                    for x in range(1,10):
                        str[i][k] = x
                        helper(str,i, k+1)
                    helper(str,i+1,1)
                if i>9 or k>9:
                    return
        helper(str,1,1)







print(Solution.solveSudoku(1, [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]))
