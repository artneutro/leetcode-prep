# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index_1 = 0
        index_2 = len(numbers)-1
        while (index_1 < index_2) :
            # Stop once the sum is same as the target
            if numbers[index_1]+numbers[index_2] == target :
                return [index_1+1, index_2+1]
            # Otherwise increase index_1 or decrease index_2 while they are lower than the target
            else :
                if (numbers[index_1+1]+numbers[index_2]) <= target :
                    index_1 += 1
                else :
                    index_2 -= 1

