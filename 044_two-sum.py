# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = 0
        value_and_index = {}
        # Store the required value in hashmap with the current index
        while index < len(nums) :
            # If found then return the indexes
            if target-nums[index] in value_and_index :
                return [value_and_index[target-nums[index]], index]
            else :
                value_and_index[nums[index]] = index
            index += 1

