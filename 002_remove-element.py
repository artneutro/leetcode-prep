# https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums) :
            # When found then delete
            if nums[i] == val :
                del nums[i]
                continue
            i = i+1
        return len(nums)









