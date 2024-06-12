# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = len(nums)
        # Base cases
        if cur == 1 or cur == 2 :
            return len(nums)
        i = 1
        while i+1<cur:
            if nums[i-1] == nums[i] and nums[i] == nums[i+1]:
                del nums[i-1]
                cur = len(nums)
            else :
                i = i+1
        return len(nums)
