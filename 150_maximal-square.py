# https://leetcode.com/problems/maximal-square/
class Solution:
    def check_for_ones(self, matrix: List[List[str]], index_row: int, index_col: int, index_row_internal: int, index_col_internal: int) -> bool:
        # Definition to check all elements of the next row and the next column column
        row = True
        col = True
        while index_row <= index_row_internal :
            if matrix[index_row][index_col_internal] != '1' :
                row = False
                break
            index_row += 1
        while index_col <= index_col_internal :
            if matrix[index_row_internal][index_col] != '1' :
                col = False
                break
            index_col += 1
        return row and col
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Variables initialization
        max_size = 0
        index_row = 0
        index_col = 0
        # Item to store the biggest square found so far
        ones_range = [[-1, -1], [-1, -1]]
        # Iterate over all rows
        while index_row < len(matrix) :
            # Iterate over all columns
            while index_col < len(matrix[0]) : 
                # If a 1 is found, iteratively check the next +1 row and +1 col
                if matrix[index_row][index_col] == '1' :
                    index_row_copy = index_row
                    index_col_copy = index_col
                    internal_index_row = index_row
                    internal_index_col = index_col
                    so_far = 0
                    while internal_index_row < len(matrix) and internal_index_col < len(matrix[0]) :
                        # Optimization: Check if the coordenates are inside the biggest square identified, so don't check again
                        if ones_range[0][0] > -1 :
                            if ones_range[0][0] < internal_index_row and internal_index_row < ones_range[1][0]\
                            and ones_range[0][1] < internal_index_col and internal_index_col < ones_range[1][1] :
                                check = True
                            else :
                                check = self.check_for_ones(matrix, index_row_copy, index_col_copy, internal_index_row, internal_index_col)
                        else :
                            check = self.check_for_ones(matrix, index_row_copy, index_col_copy, internal_index_row, internal_index_col)
                        # If the row and col are all 1, then add this to the current square
                        if check :
                            so_far += 1
                            # If the current square is bigger than the previous biggest, update solution
                            if so_far > max_size :
                                max_size = so_far
                                ones_range[0] = [index_row, index_col]
                                ones_range[1] = [internal_index_row, internal_index_col]
                        else :
                            # A 0 was found
                            break
                        internal_index_row += 1
                        internal_index_col += 1
                        # If max_size == min(rows, cols), it means the max square possible was found
                        if max_size >= min(len(matrix), len(matrix[0])) :
                            return max_size*max_size
                index_col += 1
            index_row += 1
            index_col = 0
        # Return the area of the biggest square
        return max_size*max_size

