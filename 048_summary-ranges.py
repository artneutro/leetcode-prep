# https://leetcode.com/problems/summary-ranges/
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Case no elements, return same empty set
        if len(nums) == 0 :
            return nums
        # Case one element, return the same element as str
        elif len(nums) == 1 :
            return [str(nums[0])]
        # Otherwise, create the ranges
        index = 0
        cur_set = []
        res_set = []
        # Iterate over the list, and create the ranges
        while index+1 < len(nums) :
            # For any non-last element in a sequence, append it to cur_set
            if nums[index+1] == nums[index]+1 :
                cur_set.append(nums[index])
            else :
                # For any last element in sequence or not sequenced item
                if len(cur_set) == 0 :
                    # Case not sequenced item
                    res_set.append(str(nums[index]))
                    cur_set = []
                else :
                    # Case last element in sequence
                    if cur_set[-1] == nums[index]-1 :
                    # Case element is sequenced and include the current element
                        res_set.append(str(cur_set[0])+"->"+str(nums[index]))
                        cur_set = []
                    # Case element is sequenced and not include the current element
                    else :
                        res_set.append(str(cur_set[0])+"->"+str(cur_set[-1]))
                        cur_set.append(nums[index])
            index += 1
        # Last element of nums
        if index+1 == len(nums) :
            # Case cur_set == 0, means the element is not sequenced
            if len(cur_set) == 0 :
                res_set.append(str(nums[index]))
            # Case cur_set > 0
            elif len(cur_set) > 0 :
                if cur_set[-1] == nums[index]-1 :
                # Case element is sequenced and include the last element
                    res_set.append(str(cur_set[0])+"->"+str(nums[index]))
                else :
                # Case there is a sequence but not including the last element
                    if len(cur_set) > 1 :
                        res_set.append(str(cur_set[0])+"->"+str(cur_set[-1]))
                        res_set.append(str(nums[index]))
                # Case there is a sequence of just 1 element but not including the last element
                    else :
                        res_set.append(str(cur_set[0]))
                        res_set.append(str(nums[index]))
        return res_set

