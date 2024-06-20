# https://leetcode.com/problems/search-a-2d-matrix/
class Solution:
    def binarySearch(self, array: List[int], target: int) -> bool:
        # Binary search
        if len(array) == 1 :
            return array[0] == target
        elif len(array) > 1 :
            mid = int(len(array)/2)
            if array[mid] == target :
                return True
            elif array[mid] < target :
                return self.binarySearch(array[mid:], target)
            elif array[mid] > target :
                return self.binarySearch(array[:mid], target)
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Recursively look the first element of the mid rows until 1 row
        if len(matrix) > 1 :
            if len(matrix[0]) > 0 :
                mid_row = int(len(matrix)/2)
                mid_col = 0
                if matrix[mid_row][mid_col] == target :
                    return True
                elif matrix[mid_row][mid_col] < target :
                    return self.searchMatrix(matrix[mid_row:], target)
                elif matrix[mid_row][mid_col] > target :
                    return self.searchMatrix(matrix[:mid_row], target)
        # WHen only one row left, use binary search
        elif len(matrix) == 1 :
            return self.binarySearch(matrix[0], target)
        return False

