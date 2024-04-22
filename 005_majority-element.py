# https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        checked = {}
        i = 0
        majority = [0,0]
        while (i<len(nums)) :
            if nums[i] in checked :
                checked[nums[i]] = checked[nums[i]]+1
                if checked[nums[i]] > int(len(nums)/2) :
                    return nums[i]
                if checked[nums[i]] > majority[1] :
                    majority[0] = nums[i]
                    majority[1] = checked[nums[i]]
            else :
                checked[nums[i]] = 1
                if majority[0] == 0 :
                    majority[0] = nums[i]
                    majority[1] = checked[nums[i]]
            i = i+1
        return majority[0]
# It runs in O(n)







