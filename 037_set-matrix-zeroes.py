# https://leetcode.com/problems/set-matrix-zeroes/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        index_row = 0
        index_col = 0
        while index_row < len(matrix) :
            while index_col < len(matrix[0]) :
                if matrix[index_row][index_col] == 0 :
                    internal_index_row = 0
                    internal_index_col = 0
                    # Convert all col to None
                    while internal_index_row < len(matrix) :
                        if matrix[internal_index_row][index_col] != 0 :
                            matrix[internal_index_row][index_col] = None
                        internal_index_row += 1
                    # Convert all row to None
                    while internal_index_col < len(matrix[0]) :
                        if matrix[index_row][internal_index_col] != 0 :
                            matrix[index_row][internal_index_col] = None
                        internal_index_col += 1
                index_col += 1
            index_row += 1
            index_col = 0
        # Convert all None to Zero
        index_row = 0
        index_col = 0
        while index_row < len(matrix) :
            while index_col < len(matrix[0]) :
                if matrix[index_row][index_col] == None :
                    matrix[index_row][index_col] = 0
                index_col += 1
            index_row += 1
            index_col = 0
        return matrix

