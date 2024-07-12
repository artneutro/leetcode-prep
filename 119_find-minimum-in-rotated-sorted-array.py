# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return nums[0]
        elif len(nums) == 2 :
            return min(nums[0], nums[1])
        else :
            mid = int(len(nums)/2)
            # Lower than nums[low] and lower than nums[hig] => Take Left
            if nums[mid] <= nums[0] and nums[mid] <= nums[len(nums)-1] :
                return self.findMin(nums[0:mid+1])
            # Lower than nums[low] and higher than nums[hig] => Impossible
            # Higher than nums[low] and higher than nums[hig] => Take Right
            elif nums[mid] >= nums[0] and nums[mid] >= nums[len(nums)-1] :
                return self.findMin(nums[mid:len(nums)])
            # Higher than nums[low] and lower than nums[hig] => Take Left
            elif nums[mid] >= nums[0] and nums[mid] <= nums[len(nums)-1] :
                return self.findMin(nums[0:mid+1])

