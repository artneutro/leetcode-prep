# https://leetcode.com/problems/minimum-size-subarray-sum/
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ini = 0
        end = 0
        min_length = 0
        # The moving window will be the segment sum
        sum_segment = 0
        while ini<=end and end<=len(nums) :
            if sum_segment >= target : 
                # Look for new min_length
                if min_length == 0 or min_length > end-ini :
                    min_length = end-ini
                # Move window left side
                sum_segment = sum_segment-nums[ini]
                ini = ini+1
            else :
                # Move window right side
                if end<len(nums) :
                    sum_segment = sum_segment+nums[end]
                end = end+1
        return min_length

