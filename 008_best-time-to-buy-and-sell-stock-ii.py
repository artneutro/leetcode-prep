# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
            # Look for next high
            while (high+1 < len(prices)) :
                if prices[high] < prices[high+1] :
                    high = high+1
                else :
                    break
            new_profit = prices[high] - prices[low]
            max_profit += new_profit
            low = high
        return max_profit

