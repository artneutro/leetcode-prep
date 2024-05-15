# https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cur = 0
        index = 0
        # Perform a bitwise exclusive or to check binary differences
        while index < len(nums) :
            cur = cur ^ nums[index]
            index += 1
        return cur

