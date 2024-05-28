# https://leetcode.com/problems/simplify-path/
class Solution:
    def simplifyPath(self, path: str) -> str:
        # Initialize variables
        index = 0
        fs_stack = []
        cur_str = ''
        # Go through the string and check
        while index < len(path) :
            # If the first '.' is found after a '/' and is /.
            if path[index] == '.' :
                cur_str = '.'
                index += 1
                if index < len(path) :
                    # The second '.' is found and now is /..
                    if path[index] == '.' : 
                        cur_str += '.'
                        index += 1
                        if index < len(path) :
                            # If the '/' is found then delete one level
                            if path[index] == '/' : 
                                if fs_stack[-1] == '/' :
                                    if len(fs_stack) > 1 :
                                        fs_stack.pop()
                                        if len(fs_stack) > 1 :
                                            fs_stack.pop()
                                else :
                                    fs_stack.pop()
                                index += 1
                            # Otherwise is a directory name
                            else :
                                while index < len(path) and path[index] != '/' :
                                    cur_str += path[index]
                                    index += 1
                                fs_stack.append(cur_str)
                        else :
                            # Case string finish in /..
                            if fs_stack[-1] == '/' :
                                if len(fs_stack) > 1 :
                                    fs_stack.pop()
                                    if len(fs_stack) > 1 :
                                        fs_stack.pop()
                            else :
                                fs_stack.pop()
                            index += 1
                    # Case /./
                    elif path[index] == '/' :
                        index += 1
                    # Rest of cases where it is a directory name
                    else :
                        while index < len(path) and path[index] != '/' :
                            cur_str += path[index]
                            index += 1
                        fs_stack.append(cur_str)
            # Found a new /
            elif path[index] == '/' :
                # Case root /
                if len(fs_stack) == 0 :
                    fs_stack.append('/')
                elif fs_stack[-1] != '/' :
                    fs_stack.append('/')
                index += 1
            # Rest
            else :
                cur_str = ''
                while index < len(path) and path[index] != '/' :
                    cur_str += path[index]
                    index += 1
                fs_stack.append(cur_str)
        # Construct new string from stack
        index = 0
        solution = ''
        while index < len(fs_stack) :
            solution += fs_stack[index] 
            index += 1
        if len(solution) > 1 :
            if solution[-1] == '/' :
                solution = solution[:-1]
        return solution

