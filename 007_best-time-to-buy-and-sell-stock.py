# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Base cases
        if len(prices) == 1 :
            return 0
        max_profit = 0
        low = 0
        high = 0
        # While the array is not finished
        while low<len(prices) :
            # Look for next low
            while (low+1 < len(prices)) :
                if prices[low] > prices[low+1] :
                    low = low+1
                else :
                    high = low+1
                    break
            # If it reached the end of array, return current max_profit
            if low+1 == len(prices) :
                return max_profit
            # Look for max value after current low
            higher_value = max(prices[low:])
            # Get the latest index of this value
            higher_value_last_index = len(prices[low:]) - 1 - (prices[low:])[::-1].index(higher_value)
            high = len(prices)-len(prices[low:])+higher_value_last_index
            # Look for min value between current low and last high
            if low < high :
                lower_value = min(prices[low:high])
                low = len(prices)-len(prices[low:])+prices[low:].index(lower_value)
            else :
                return max_profit
            # Case when no higher exists
            if higher_value < lower_value :
                return max_profit
            # Case when higher exists
            else :
                new_profit = higher_value - lower_value
                if new_profit > max_profit :
                    max_profit = new_profit
                    low = high
                else :
                    low = high
        return 0
