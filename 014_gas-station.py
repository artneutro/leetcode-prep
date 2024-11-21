class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int: 
        # Main index
        index = 0
        # Current initial index and cumulative sum
        index_ini = 0
        cumul_ini = 0
        # Overall positive and negative sum to avoid second round
        sum_pos = 0
        sum_neg = 0
        # Check all elements and get the (gas[index] - cost[index]) value to split
        while index < len(gas) :
            if index == len(gas)-1 :
                # Once it reach the end
                if gas[index] - cost[index] < 0 :
                    sum_neg = sum_neg + (gas[index] - cost[index])
                else :
                    sum_pos = sum_pos + (gas[index] - cost[index])
                # Final overall count to confirm if the last section positive can perform the round
                # After reduce using the negative values
                if (sum_pos + sum_neg) >= 0 : 
                    return index_ini
                else :
                    return -1
            else :
                # All the rest
                if gas[index] - cost[index] < 0 :
                    # If current line negative, sum into negative
                    sum_neg = sum_neg + (gas[index] - cost[index])
                    # If the current cumulative sum is negative, change the index ini to the next one
                    if (cumul_ini + (gas[index] - cost[index])) < 0 : 
                        index_ini = index+1
                        cumul_ini = 0
                    else :
                        # If not, then continue accumulating
                        cumul_ini += (gas[index] - cost[index])
                else :
                    # If current line positive, sum into positive
                    sum_pos = sum_pos + (gas[index] - cost[index])
                    cumul_ini += (gas[index] - cost[index])
            index += 1







