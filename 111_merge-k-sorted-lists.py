# https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def quicksortLists(self, lists: List[Optional[ListNode]], ini: int, end: int) -> List[Optional[ListNode]]:
        # Quicksort customized to order based on the first value of an array of linked lists
        if len(lists[ini:end]) == 0 or len(lists[ini:end]) == 1 or end <= ini:
            # Nothing if the size if 0 or 1
            return lists
        elif len(lists[ini:end]) == 2 :
            # If size is 2, check if if must be reversed
            if lists[ini].val > lists[ini+1].val :
                temp = lists.pop(ini)
                lists.insert(ini+1, temp)
        else :
            # If size is larger than 2, move all lower than first element before it
            mid_point = ini
            index = end-1
            while index > mid_point :
                if lists[index].val < lists[mid_point].val :
                    temp = lists.pop(index)
                    lists.insert(mid_point, temp)
                    mid_point += 1
                    continue
                index -= 1
            # Recursively perform quicksort for lower values and higher values based on mid_point
            self.quicksortLists(lists, ini, mid_point)
            self.quicksortLists(lists, mid_point+1, end)
    def binarySearchLists(self, lists: List[Optional[ListNode]], cur_low: ListNode, ini: int, end: int) -> List[Optional[ListNode]]: 
        # Binary search custommized to work with the first element of linked lists in array
        while ini <= end :
            mid = int((end-ini)/2)
            if mid == 0 :
                # Element was not found, insert it in the position it must be
                if len(lists[ini:end]) == 0 :
                    lists.insert(ini, cur_low)
                    break
                elif len(lists[ini:end]) == 1 :
                # Element was not found, check if the current element in its posistion is lower or higher
                    if lists[ini+mid].val <= cur_low.val :
                        lists.insert(ini+1, cur_low)
                        break
                    else :
                        lists.insert(ini, cur_low)
                        break
            elif lists[ini+mid].val == cur_low.val :
                # Element was found, insert it in the position it must be
                lists.insert(ini+mid, cur_low)
                break
            elif lists[ini+mid].val < cur_low.val :
                ini = ini+mid
            elif lists[ini+mid].val > cur_low.val :
                end = ini+mid
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Base cases
        if len(lists) == 0 :
            return None
        if len(lists) == 1 :
            return lists[0]
        # Remove all empty linked lists
        index = 0
        while index < len(lists) :
            if lists[index] == None :
                lists.pop(index)
                continue
            index += 1
        # Sort the array according to first node value using quicksort
        self.quicksortLists(lists, 0, len(lists))
        # Every iteration, get the first element of the first list in the array
        solution = None
        final_list = None
        while len(lists) > 0 :
            if lists[0] == None :
                lists.pop(0)
            else :
                cur_low = lists.pop(0)
                # Then, add the element to the final list
                new_node = ListNode(cur_low.val)
                if solution == None :
                    final_list = new_node
                    solution = final_list
                else :
                    final_list.next = new_node
                    final_list = final_list.next
                # Re-position this list in the array as per the next node value using binary search
                if cur_low.next != None :
                    cur_low = cur_low.next
                    self.binarySearchLists(lists, cur_low, 0, len(lists))
        return solution

