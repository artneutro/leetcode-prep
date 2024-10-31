# https://leetcode.com/problems/generate-parentheses/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solution = {}
        # Queue with elements [string, total_left_par, total_right_par, open_left_par]
        queue = []
        queue.append(['(', 1, 0, 1])
        while len(queue) > 0 :
            next_path = queue.pop(0)
            total_left_par = next_path[1]
            total_right_par = next_path[2]
            open_left_par = next_path[3]
            # If we have a full path, add it to solution
            if total_left_par+total_right_par == 2*n :
                if next_path[0] not in solution :
                    solution[next_path[0]] = 1
                continue
            # If all left parenthesis were already placed
            if total_left_par == n :
                # Then, put all the right parenthesis needed
                right_par = 0
                while total_right_par+right_par < n :
                    next_path[0] += ')'
                    right_par += 1
                # If the complete string is not in the solution, add it
                if next_path[0] not in solution :
                    solution[next_path[0]] = 1
            else :
                # If there are left parenthesis to put
                left_option = next_path[0]+'('
                queue.append([left_option, total_left_par+1, total_right_par, open_left_par+1])
                # Add the path with right parenthesis only if the number of left is higher
                if total_left_par > total_right_par :
                    right_option = next_path[0]+')'
                    queue.append([right_option, total_left_par, total_right_par+1, open_left_par-1])
        return list(solution)

