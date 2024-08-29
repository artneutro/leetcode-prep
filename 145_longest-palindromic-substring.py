# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        longest_pal = ''
        main_index = 0
        left_index = 0
        righ_index = 0
        while main_index < len(s) :
            print(s[main_index])
            # Try odd with main_index as central
            left_index = main_index-1
            righ_index = main_index+1
            while left_index > -1 and righ_index < len(s) : 
                if s[left_index] != s[righ_index] :
                    if (righ_index-left_index-1) > longest :
                        longest = righ_index-left_index-1
                        longest_pal = s[left_index+1:righ_index]
                    break
                left_index -= 1
                righ_index += 1
            # Reached one of the sides
            if left_index == -1 or righ_index == len(s) : 
                left_index += 1
                righ_index -= 1
                if (righ_index-left_index+1) > longest :
                    longest = righ_index-left_index+1
                    longest_pal = s[left_index:righ_index+1]
            # Try even with main_index and left_index as central
            left_index = main_index-1
            righ_index = main_index
            while left_index > -1 and righ_index < len(s) : 
                if s[left_index] != s[righ_index] :
                    if (righ_index-left_index-1) > longest :
                        longest = righ_index-left_index-1
                        longest_pal = s[left_index+1:righ_index]
                    break
                left_index -= 1
                righ_index += 1
            # Reached one of the sides
            if left_index == -1 or righ_index == len(s) : 
                left_index += 1
                righ_index -= 1
                if (righ_index-left_index+1) > longest :
                    longest = righ_index-left_index+1
                    longest_pal = s[left_index:righ_index+1]
            # Try even with righ_index and main_index as central
            left_index = main_index
            righ_index = main_index+1
            while left_index > -1 and righ_index < len(s) : 
                if s[left_index] != s[righ_index] :
                    if (righ_index-left_index-1) > longest :
                        longest = righ_index-left_index-1
                        longest_pal = s[left_index+1:righ_index]
                    break
                left_index -= 1
                righ_index += 1
            # Reached one of the sides
            if left_index == -1 or righ_index == len(s) :  
                left_index += 1
                righ_index -= 1
                if (righ_index-left_index+1) > longest :
                    longest = righ_index-left_index+1
                    longest_pal = s[left_index:righ_index+1]
            main_index += 1
        return longest_pal

