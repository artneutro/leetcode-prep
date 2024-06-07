# https://leetcode.com/problems/remove-duplicates-from-sorted-array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        cur = len(nums)
        while i<cur:
            # If duplicate found, remove it
            if nums[i-1] == nums[i] :
                del nums[i-1]
                cur = len(nums)
            else :
                i = i+1
        return len(nums)
        
