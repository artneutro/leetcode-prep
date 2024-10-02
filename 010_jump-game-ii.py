# https://leetcode.com/problems/jump-game-ii/
class Solution:
    def jump(self, nums: List[int]) -> int:
        # Border case
        if len(nums) == 1 :
            return 0
        # Hashtable for quick look
        nexts = {}
        # Queue for FIFO
        queue = []
        # Initialize 
        nexts[0] = 1
        queue.append((0, 0))
        # Enqueue the sum of current index + all options, then check next possibility
        while len(queue) > 0 :
            # Get next index from queue
            next_index = queue.pop(0)
            del nexts[next_index[0]]
            # If index is last or between the range, it is possible
            if (next_index[0] == len(nums)-1) or (len(nums)-1-next_index[0] <= nums[next_index[0]]):
                return next_index[1]+1
            # If it is not last index, then enqueue all possible paths
            for i in range(nums[next_index[0]]) :
                # If sum is over the last index, break this iteration to improve time
                if next_index[0]+i+1 > len(nums) :
                    break
                else : 
                    if next_index[0]+i+1 not in nexts :
                        # Improvement for large cases
                        if next_index[0]+i+1 == len(nums)-1 :
                            return next_index[1]+1
                        nexts[next_index[0]+i+1] = 1
                        queue.append((next_index[0]+i+1, next_index[1]+1))
        return -1
        
