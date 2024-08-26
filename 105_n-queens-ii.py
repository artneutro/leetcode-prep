# https://leetcode.com/problems/n-queens-ii/
class Solution:
    def totalNQueens(self, n: int) -> int:
        solutions = 0
        current_board = [0]*n
        # Represent the row number as the index and the col number as the content
        # Row will always be different, col must required to:
        # 1. All *i and *j must be lower than n
        # 2. Not be any of the previous col numbers
        # 3. Absolute value of Ai-Bi and Aj-Bj must be different for each pair 
        index = 0
        while index < n and index > -1:
            # 1. All *i and *j must be lower than n
            if current_board[index] >= n :
                current_board[index] = 0
                index = index-1
                current_board[index] += 1
                continue
            # 2. Not be any of the previous col numbers
            if current_board[index] in current_board[:index] :
                current_board[index] = current_board[index]+1
                continue
            # 3. Absolute value of Ai-Bi and Aj-Bj must be different for each pair 
            iterator = 0
            while iterator < index :
                if abs(current_board[index]-current_board[iterator]) == abs(index-iterator) :
                    break
                iterator += 1
            if iterator < index and abs(current_board[index]-current_board[iterator]) == abs(index-iterator) :
                current_board[index] = current_board[index]+1
                continue
            # A solution was found, as it passed all checks
            if index == n-1 :
                solutions += 1
                current_board[index] = 0
                index = index-1
                current_board[index] += 1
                continue
            index += 1
        return solutions

