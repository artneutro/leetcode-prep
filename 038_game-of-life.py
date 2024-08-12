# https://leetcode.com/problems/game-of-life/
class Solution:
    def check_item(self, board: List[List[int]], index_row: int, index_col: int) -> None :
        # Check if the cell is alive or dead
        dead_or_alive = -1
        if board[index_row][index_col] == 0 or board[index_row][index_col] == -1 :
            dead_or_alive = 0
        elif board[index_row][index_col] == 1 or board[index_row][index_col] == -2 :
            dead_or_alive = 1
        # Check how many zeroes and ones it has as neighbours
        count_zeroes = 0
        count_ones = 0
        # i-1, j-1
        if index_row > 0 and index_col > 0 :
            if board[index_row-1][index_col-1] == 0 or board[index_row-1][index_col-1] == -1 :
                count_zeroes += 1
            elif board[index_row-1][index_col-1] == 1 or board[index_row-1][index_col-1] == -2 :
                count_ones += 1
        # i-1, j
        if index_row > 0 :
            if board[index_row-1][index_col] == 0 or board[index_row-1][index_col] == -1 :
                count_zeroes += 1
            elif board[index_row-1][index_col] == 1 or board[index_row-1][index_col] == -2 :
                count_ones += 1
        # i-1, j+1
        if index_row > 0 and index_col < len(board[0])-1 :
            if board[index_row-1][index_col+1] == 0 or board[index_row-1][index_col+1] == -1 :
                count_zeroes += 1
            elif board[index_row-1][index_col+1] == 1 or board[index_row-1][index_col+1] == -2 :
                count_ones += 1
        # i, j-1
        if index_col > 0 :
            if board[index_row][index_col-1] == 0 or board[index_row][index_col-1] == -1 :
                count_zeroes += 1
            elif board[index_row][index_col-1] == 1 or board[index_row][index_col-1] == -2 :
                count_ones += 1
        # i, j+1
        if index_col < len(board[0])-1 :
            if board[index_row][index_col+1] == 0 or board[index_row][index_col+1] == -1 :
                count_zeroes += 1
            elif board[index_row][index_col+1] == 1 or board[index_row][index_col+1] == -2 :
                count_ones += 1
        # i+1, j-1
        if index_row < len(board)-1 and index_col > 0 :
            if board[index_row+1][index_col-1] == 0 or board[index_row+1][index_col-1] == -1 :
                count_zeroes += 1
            elif board[index_row+1][index_col-1] == 1 or board[index_row+1][index_col-1] == -2 :
                count_ones += 1
        # i+1, j
        if index_row < len(board)-1 :
            if board[index_row+1][index_col] == 0 or board[index_row+1][index_col] == -1 :
                count_zeroes += 1
            elif board[index_row+1][index_col] == 1 or board[index_row+1][index_col] == -2 :
                count_ones += 1
        # i+1, j+1
        if index_row < len(board)-1 and index_col < len(board[0])-1 :
            if board[index_row+1][index_col+1] == 0 or board[index_row+1][index_col+1] == -1 :
                count_zeroes += 1
            elif board[index_row+1][index_col+1] == 1 or board[index_row+1][index_col+1] == -2 :
                count_ones += 1
        # Check cell next generation
        if dead_or_alive == 0 :
            # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
            if count_ones == 3 :
                board[index_row][index_col] = -1
        else :
            # Any live cell with fewer than two live neighbors dies as if caused by under-population.
            # Any live cell with more than three live neighbors dies, as if by over-population.
            if count_ones < 2 or count_ones > 3 :
                board[index_row][index_col] = -2
            # Any live cell with two or three live neighbors lives on to the next generation.
    def set_board(self, board: List[List[int]]) -> None:
        # Set the next generation based on results from previous generation
        index_row = 0
        index_col = 0
        while index_row < len(board) :
            while index_col < len(board[0]) :
                if board[index_row][index_col] == -2 :
                    board[index_row][index_col] = 0
                elif board[index_row][index_col] == -1 :
                    board[index_row][index_col] = 1
                index_col += 1
            index_col = 0
            index_row += 1
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        index_row = 0
        index_col = 0
        while index_row < len(board) :
            while index_col < len(board[0]) :
                # Check next generation for each cell based on game rules
                self.check_item(board, index_row, index_col)
                index_col += 1
            index_col = 0
            index_row += 1
        # Perform next board config
        self.set_board(board)
        return board

