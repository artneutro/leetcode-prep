# https://leetcode.com/problems/valid-sudoku/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        # Check rows
        row_index = 0
        column_index = 0
        while row_index < len(board) :
            check = []
            while column_index < len(board) :
                if board[row_index][column_index] == '.' :
                    pass
                elif board[row_index][column_index] not in check \
                and board[row_index][column_index] in valid_values :
                    check.append(board[row_index][column_index])
                else :
                    return False
                column_index += 1
            row_index += 1
            column_index = 0
        # Check columns
        row_index = 0
        column_index = 0
        while column_index < len(board) :
            check = []
            while row_index < len(board) :
                if board[row_index][column_index] == '.' :
                    pass
                elif board[row_index][column_index] not in check \
                and board[row_index][column_index] in valid_values :
                    check.append(board[row_index][column_index])
                else :
                    return False
                row_index += 1
            column_index += 1
            row_index = 0
        # Check sub-boxes
        row_index = 0
        column_index = 0
        row_phase = 0
        column_phase = 0
        while row_phase < len(board) :
            row_phase += 3
            while column_phase < len(board) :
                check = []
                column_phase += 3
                # Check sub-boxes rows
                while row_index < row_phase :
                    # Check sub-boxes columns
                    while column_index < column_phase :
                        #print(board[row_index][column_index], row_index, column_index)
                        if board[row_index][column_index] == '.' :
                            pass
                        elif board[row_index][column_index] not in check \
                        and board[row_index][column_index] in valid_values :
                            check.append(board[row_index][column_index])
                        else :
                            return False
                        column_index += 1
                    row_index += 1
                    # Reset column_index
                    column_index -= 3
                # Each time both rows and columns reach sub-box max phases
                # Reset row_index
                row_index -= 3
                # Fix column_index when reach last in sub-box
                column_index += 3
            # Fix row_index when reach last in sub-box
            row_index += 3
            # Reset column_index when reach last 
            column_index = 0
            # Reset column_phase when reach last
            column_phase = 0
        return True

