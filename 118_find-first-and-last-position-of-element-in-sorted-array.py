# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def binarySearchLowIndex(self, nums: List[int], target: int, ini: int, end: int, sol: List[int]) -> List[int]:
        # This def is to look for the lower index
        if ini == end :
            if nums[ini] == target :
                if ini < sol[0] :
                    sol[0] = ini
                if ini > sol[1] :
                    sol[1] = ini
        elif ini+1 == end :
            if nums[ini] == target :
                if ini < sol[0] :
                    sol[0] = ini
                if ini > sol[1] :
                    sol[1] = ini
            if nums[end] == target :
                if end < sol[0] :
                    sol[0] = end
                if end > sol[1] :
                    sol[1] = end
        elif ini < end :
            mid = int((end-ini)/2)
            if nums[ini+mid] >= target :
                sol = self.binarySearchLowIndex(nums, target, ini, ini+mid, sol)
            else :
                sol = self.binarySearchLowIndex(nums, target, ini+mid, end, sol)
        return sol
    def binarySearchHigIndex(self, nums: List[int], target: int, ini: int, end: int, sol: List[int]) -> List[int]:
        # This def is to look for the upper index
        if ini == end :
            if nums[ini] == target :
                if ini < sol[0] :
                    sol[0] = ini
                if ini > sol[1] :
                    sol[1] = ini
        elif ini+1 == end :
            if nums[ini] == target :
                if ini < sol[0] :
                    sol[0] = ini
                if ini > sol[1] :
                    sol[1] = ini
            if nums[end] == target :
                if end < sol[0] :
                    sol[0] = end
                if end > sol[1] :
                    sol[1] = end
        elif ini < end :
            mid = int((end-ini)/2)
            print(sol, mid)
            if nums[ini+mid] > target :
                sol = self.binarySearchHigIndex(nums, target, ini, ini+mid, sol)
            else :
                sol = self.binarySearchHigIndex(nums, target, ini+mid, end, sol)
        return sol
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Solution is O(logn)+O(logn) = O(2*logn) ==> O(logn)
        solution = [len(nums),-1]
        # Look for the lower index
        solution = self.binarySearchLowIndex(nums, target, 0, len(nums)-1, solution)
        # Look for the upper index
        solution = self.binarySearchHigIndex(nums, target, 0, len(nums)-1, solution)
        if solution[0] == len(nums) :
            solution[0] = -1
        return solution
        
