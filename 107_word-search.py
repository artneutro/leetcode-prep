# https://leetcode.com/problems/word-search/
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Optimization: Check if all word characters are in the board
        index = 0
        while index < len(word) :
            i, j = 0, 0
            is_in = False
            while i < len(board) and not is_in :
                while j < len(board[0]) and not is_in :
                    if board[i][j] == word[index] :
                        is_in = True
                    j += 1
                i += 1
                j = 0
            if is_in :
                index += 1
            else :
                break
        if not is_in :
            return False
        # Variables initialization
        paths = []
        current_path = []
        new_path = []
        # Loop to look for first char
        index_row = 0
        while index_row < len(board) :
            index_col = 0
            while index_col < len(board[0]) :
                # External loop to look for the first element
                if board[index_row][index_col] == word[0] :
                    paths.append([(index_row, index_col)])
                    # Case 1x1
                    if len(paths[0]) == len(word) :
                        return True
                    # Internal loop to look for next characters
                    while len(paths) > 0 :
                        # Use stack to increase every path found in order (DFS)
                        current_path = paths.pop(-1)
                        # Get last node of current path
                        current_coordenates = current_path[-1]
                        i = current_coordenates[0]
                        j = current_coordenates[1]
                        # i-1, j
                        if i-1 >= 0 and len(current_path) < len(word) : 
                            if board[i-1][j] == word[len(current_path)] : 
                                if (i-1, j) not in current_path :
                                    new_path = current_path.copy()
                                    new_path.append((i-1, j))
                                    if len(new_path) == len(word) :
                                        return True
                                    else :
                                        paths.append(new_path)
                        # i, j-1
                        if j-1 >= 0 and len(current_path) < len(word) : 
                            if board[i][j-1] == word[len(current_path)] : 
                                if (i, j-1) not in current_path :
                                    new_path = current_path.copy()
                                    new_path.append((i, j-1))
                                    if len(new_path) == len(word) :
                                        return True
                                    else :
                                        paths.append(new_path)
                        # i+1, j
                        if i+1 < len(board) and len(current_path) < len(word) : 
                            if board[i+1][j] == word[len(current_path)] : 
                                if (i+1, j) not in current_path :
                                    new_path = current_path.copy()
                                    new_path.append((i+1, j))
                                    if len(new_path) == len(word) :
                                        return True
                                    else :
                                        paths.append(new_path)
                        # i, j+1
                        if j+1 < len(board[0]) and len(current_path) < len(word) : 
                            if board[i][j+1] == word[len(current_path)] : 
                                if (i, j+1) not in current_path :
                                    new_path = current_path.copy()
                                    new_path.append((i, j+1))
                                    if len(new_path) == len(word) :
                                        return True
                                    else :
                                        paths.append(new_path)
                # If not found, reset word_index, coordenates and current_paths
                paths = []
                index_col += 1
            index_row += 1
        return False

