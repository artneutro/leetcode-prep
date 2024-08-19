# https://leetcode.com/problems/rotate-image/
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 1 :
            return matrix
        # Get initial value
        curr_value = None
        next_value = None
        maxi_value = len(matrix)-1
        # Horizontal Up
        index_i_h_u = 0
        index_j_h_u = 0
        # Vertical Right
        index_i_v_r = 0
        index_j_v_r = len(matrix)-1
        # Horizontal Down
        index_i_h_d = len(matrix)-1
        index_j_h_d = len(matrix)-1
        # Vertical Left
        index_i_v_l = len(matrix)-1
        index_j_v_l = 0
        while index_i_h_u < int(len(matrix)/2) :
            while index_j_h_u < maxi_value : 
                curr_value = matrix[index_i_h_u][index_j_h_u]
                # Horizontal Up
                next_value = matrix[index_i_v_r][index_j_v_r]
                matrix[index_i_v_r][index_j_v_r] = curr_value
                curr_value = next_value
                # Vertical Right
                next_value = matrix[index_i_h_d][index_j_h_d]
                matrix[index_i_h_d][index_j_h_d] = curr_value
                curr_value = next_value
                # Horizontal Down
                next_value = matrix[index_i_v_l][index_j_v_l]
                matrix[index_i_v_l][index_j_v_l] = curr_value
                curr_value = next_value
                # Vertical Left
                next_value = matrix[index_i_h_u][index_j_h_u]
                matrix[index_i_h_u][index_j_h_u] = curr_value
                curr_value = next_value
                # Add up
                index_j_h_u += 1
                index_i_v_r += 1
                index_j_h_d -= 1
                index_i_v_l -= 1
            # Reduce to internal sub-matrix
            maxi_value -= 1
            # Horizontal Up
            index_i_h_u += 1
            index_j_h_u = index_i_h_u
            # Vertical Right
            index_i_v_r = index_i_h_u
            index_j_v_r -= 1
            # Horizontal Down
            index_i_h_d = index_j_v_r
            index_j_h_d = index_j_v_r
            # Vertical Left
            index_i_v_l = index_j_v_r
            index_j_v_l = index_i_h_u
        return matrix

