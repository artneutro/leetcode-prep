# https://leetcode.com/problems/search-insert-position/
class Solution:
    def indexKeeper(self, nums: List[int], target: int, ini: int, end: int) -> int:
        # Get middle point
        mid = (end-ini)//2
        #print(nums[ini:end], target, ini, mid, end)
        # When there is only one element, check if the target is lower, same or higher
        if (end-ini) == 1 :
            if target < nums[ini] :
                return ini
            elif nums[ini] == target :
                return ini
            elif target > nums[ini] :
                return ini+1
        # Recursively move ini and end depending on the target 
        elif (end-ini) > 1 :
            if target < nums[ini+mid] :
                return self.indexKeeper(nums, target, ini, end-mid)
            elif nums[ini+mid] == target :
                return ini+mid
            elif target > nums[ini+mid] :
                return self.indexKeeper(nums, target, ini+mid, end)
        else : 
            return mid
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Base cases (when the target is lower than first element)
        if target < nums[0] :
            return 0
        # Base cases (when the target is higher than last element)
        elif target > nums[-1] :
            return len(nums)
        # Otherwise
        else :
            return self.indexKeeper(nums, target, 0, len(nums))

