# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        solution = ListNode()
        output = solution
        # Case one or both empty lists
        if list1 == None and list2 == None :
            return None
        elif list1 == None and list2 != None :
            return list2
        elif list1 != None and list2 == None :
            return list1
        # Case both non-empty initialization
        if list1 != None and list2 != None :
            if list1.val <= list2.val :
                solution.val = list1.val
                list1 = list1.next
            else :
                solution.val = list2.val
                list2 = list2.next
        # Iterate over the 2 lists until one ends
        while list1 != None and list2 != None :
            if list1.val <= list2.val :
                new_node = ListNode()
                new_node.val = list1.val
                list1 = list1.next
                solution.next = new_node
                solution = solution.next
            else :
                new_node = ListNode()
                new_node.val = list2.val
                list2 = list2.next
                solution.next = new_node
                solution = solution.next
        # Add the remainder items
        if list1 == None :
            solution.next = list2
        else :
            solution.next = list1
        return output

