# https://leetcode.com/problems/jump-game/
class Solution:
    # There is an option checking max of (current index + current index val) sub-array, but it has a bug, so for now this is my solution
    def canJump(self, nums: List[int]) -> bool:
        # Hashtable for quick look
        nexts = {}
        # Queue for FIFO
        queue = []
        # Initialize 
        nexts[0] = 1
        queue.append(0)
        # Enqueue the sum of current index + all options, then check next possibility
        while len(queue) > 0 :
            # Get next index from queue
            next_index = queue.pop(0)
            del nexts[next_index]
            # If index is last or between the range, it is possible
            if (next_index == len(nums)-1) or (len(nums)-1-next_index <= nums[next_index]):
                return True
            # If it is not last index, then enqueue all possible paths
            for i in range(nums[next_index]) :
                # If sum is over the last index, break this iteration to improve time
                if next_index+i+1 > len(nums) :
                    break
                else : 
                    if next_index+i+1 not in nexts :
                        # Improvement for large cases
                        if next_index+i+1 == len(nums)-1 :
                            return True
                        nexts[next_index+i+1] = 1
                        queue.append(next_index+i+1)
        return False

