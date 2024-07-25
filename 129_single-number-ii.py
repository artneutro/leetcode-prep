# https://leetcode.com/problems/single-number-ii/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        items = {}
        repeated = {}
        index = 0
        while index < len(nums) :
            if nums[index] in items :
                # If the item was found the third time, removed
                if nums[index] in repeated :
                    del repeated[nums[index]]
                    del items[nums[index]]
                # If the item was found the second time, repeated
                else :
                    repeated[nums[index]] = 1
            # If the item was found the first time, itemized
            else :
                items[nums[index]] = 1
            index += 1
        # Return the only element in items at the end
        return list(items.keys())[0]

