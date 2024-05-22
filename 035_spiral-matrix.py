# https://leetcode.com/problems/spiral-matrix/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Indexes to be used to go through the matrix
        index_row = 0
        index_col = 0
        # Counters to check if all elements were shown
        counter = 0
        matrix_size = len(matrix)*len(matrix[0])
        # Move inside the current matrix sizes
        cur_row_min = 0
        cur_col_min = -1
        cur_row_max = len(matrix)
        cur_col_max = len(matrix[0])
        # Store the solution
        solution = []
        while counter < matrix_size : 
            # Loop Current Up Row
            while index_col < cur_col_max and counter < matrix_size :
                solution.append(matrix[index_row][index_col])
                counter += 1
                index_col += 1
            index_col -= 1
            index_row += 1
            # Loop Current Right Column
            while index_row < cur_row_max and counter < matrix_size :
                solution.append(matrix[index_row][index_col])
                counter += 1
                index_row += 1
            index_row -= 1
            index_col -= 1
            # Loop Current Down Row
            while index_col > cur_col_min and counter < matrix_size :
                solution.append(matrix[index_row][index_col])
                counter += 1
                index_col -= 1
            index_col += 1
            index_row -= 1
            # Loop Current Left Column
            while index_row > cur_row_min and counter < matrix_size :
                solution.append(matrix[index_row][index_col])
                counter += 1
                index_row -= 1
            index_row += 1
            index_col += 1
            # Set the new matrix sizes
            cur_row_min += 1
            cur_col_min += 1
            cur_row_max -= 1
            cur_col_max -= 1
        return solution

