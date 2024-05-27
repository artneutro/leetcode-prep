# https://leetcode.com/problems/merge-sorted-array/description/ 

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Create 2 pointers (one per array)
        nums1_ptr = 0
        nums2_ptr = 0
        # Loop to insert all elements from array2 to array1
        while (nums2_ptr < n) :
            # Look for next bigger number to insert in current index of pointer1 
            if nums1[nums1_ptr] <= nums2[nums2_ptr] and nums1_ptr < m+nums2_ptr: 
                nums1_ptr += 1
            else :
                nums1.insert(nums1_ptr, nums2[nums2_ptr])
                nums1_ptr += 1
                nums2_ptr += 1
        # Remove all zero elements left
        i = 0
        while (i < n) :
            nums1.pop()
            i += 1
        





