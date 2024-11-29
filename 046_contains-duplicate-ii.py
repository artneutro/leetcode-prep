# https://leetcode.com/problems/contains-duplicate-ii/
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = {}
        index = 0
        while index < len(nums) :
            if nums[index] not in mapping :
                mapping[nums[index]] = [index]
            else :
                for other_index in mapping[nums[index]] :
                    if abs(index-other_index) <= k :
                        return True
                mapping[nums[index]].append(index)
            index += 1
        return False




