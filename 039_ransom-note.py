# https://leetcode.com/problems/ransom-note/
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Store the magazine values in a hashmap with the number of repetitions
        valid_values = {}
        index = 0
        while index < len(magazine) :
            if magazine[index] in valid_values :
                valid_values[magazine[index]] += 1 
            else :
                valid_values[magazine[index]] = 1
            index += 1
        # Check the note characters and evaluate if they are in the magazine
        index = 0
        while index < len(ransomNote) :
            if ransomNote[index] in valid_values :
                if valid_values[ransomNote[index]] > 0 :
                    valid_values[ransomNote[index]] -= 1
                else :
                    return False
            else :
                return False
            index += 1
        # Return True only after all checks passed
        return True
        
