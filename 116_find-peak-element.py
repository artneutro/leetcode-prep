# https://leetcode.com/problems/find-peak-element/
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Base cases (len 1 or 2)
        if len(nums) == 1 :
            return 0
        elif len(nums) == 2 :
            if nums[0] > nums[1] :
                return 0
            else :
                return 1
        # Case pos 0 is peak
        elif nums[0] > nums[1] :
            return 0
        # Case pos len-1 is peak
        elif nums[-2] < nums[-1] :
            return len(nums)-1
        # Otherwise iterate over the array to look for a peak
        else: 
            index = 1
            while index+1 < len(nums) :
                if nums[index-1] < nums[index]\
                and nums[index] > nums[index+1] :
                    return index
                index += 1
        return 0

