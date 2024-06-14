# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Variables initialization
        product = 1
        zeroes = []
        solution = []
        # Iterates over the nums and update product
        index = 0
        while index < len(nums) :
            # If a zero is found, add the index on the zeroes list
            if nums[index] == 0 :
                zeroes.append(index)
                index += 1
                continue
            product *= nums[index]
            index += 1
        # If more than 1 zero, all result must be zeroes
        if len(zeroes) > 1 :
            return len(nums)*[0]
        # If just 1 zero, all result must be zeroes except the zero position
        elif len(zeroes) == 1 :
            return ([0]*zeroes[0])+[product]+([0]*(len(nums)-zeroes[0]-1))
        # Otherwise multiply with 1/n where n is the value in nums concluding in O(n)
        else :
            index = 0
            while index < len(nums) :
                solution.append(int(product*(1/nums[index])))
                index += 1
            return solution

