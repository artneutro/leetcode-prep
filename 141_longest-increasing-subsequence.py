# https://leetcode.com/problems/longest-increasing-subsequence/
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Create a parallel array with the max path size before index
        longest_sub = [0]*len(nums)
        longest_sub[0] = 1
        # Iterate over the elements of nums
        index = 1
        while index < len(nums) :
            # For each element compare with all previous 
            cur_max = 0
            index_internal = index-1
            while index_internal >= 0 :
                # If lower, then check if the max path size is larger than the current max
                if nums[index_internal] < nums[index]\
                and longest_sub[index_internal] > cur_max :
                    cur_max = longest_sub[index_internal]
                index_internal -= 1
            # Assign the max path + 1 to the current index
            longest_sub[index] = cur_max+1
            index += 1
        # Return longer path found
        return max(longest_sub)

