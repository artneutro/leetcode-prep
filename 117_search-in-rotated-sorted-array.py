# https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Base cases
        if len(nums) == 0 :
            return -1
        elif len(nums) == 1 and nums[0] == target :
            return 0
        elif len(nums) == 1 and nums[0] != target :
            return -1
        # Main search
        else :
            ini = 0
            end = len(nums)-1
            while ini <= end :
                # Final cases
                if ini == end and nums[ini] == target :
                    return ini
                elif ini == end and nums[ini] != target :
                    return -1
                elif (end-ini) < 2 :
                    if nums[ini] == target :
                        return ini
                    elif nums[end] == target :
                        return end
                    else :
                        return -1
                # Iteratively halve the array depending on mid value and extremes values
                elif ini < end :
                    mid = ini+int((end-ini)/2)
                    if nums[mid] == target :
                        return mid
                    elif nums[mid] < target and nums[ini] <= target and nums[end] <= target :
                        # Special case where all 3 are lower, it could be in any of the 2 sides
                        if nums[ini] < nums[mid] :
                            ini = mid
                        else :
                            end = mid
                    elif nums[mid] < target and nums[ini] <= target and nums[end] >= target :
                        ini = mid
                    elif nums[mid] < target and nums[ini] >= target and nums[end] >= target :
                        ini = mid
                    elif nums[mid] < target and nums[ini] >= target and nums[end] <= target :
                        return -1
                    elif nums[mid] > target and nums[ini] <= target and nums[end] <= target :
                        end = mid
                    elif nums[mid] > target and nums[ini] <= target and nums[end] >= target :
                        end = mid
                    elif nums[mid] > target and nums[ini] >= target and nums[end] >= target :
                        # Special case where all 3 are higher, it could be in any of the 2 sides
                        if nums[ini] > nums[mid] :
                            end = mid
                        else :
                            ini = mid
                    elif nums[mid] > target and nums[ini] >= target and nums[end] <= target :
                        return -1
                else :
                    return -1
        return -1

