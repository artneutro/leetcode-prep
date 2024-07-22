# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = -10**4
        max_sum_so_far = -10**4
        # Apply Kadane's Algorithm
        index = 0
        while index < len(nums) :
            # [1,2]
            if cur_sum+nums[index] > nums[index] :
                cur_sum += nums[index]
            elif cur_sum+nums[index] == nums[index] :
                cur_sum = nums[index]
            elif nums[index] >= cur_sum :
                cur_sum = nums[index]
            else :
                cur_sum += nums[index]
            # If current sum is higher than max sum, apply new high
            if cur_sum > max_sum_so_far :
                max_sum_so_far = cur_sum
            index += 1
        return max_sum_so_far

