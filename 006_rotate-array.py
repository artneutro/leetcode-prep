# https://leetcode.com/problems/rotate-array/
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while (i < k) :
            item = nums.pop()
            nums.insert(0,item)
            i = i+1
        
