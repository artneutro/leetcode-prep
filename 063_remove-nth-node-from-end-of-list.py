# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Elements storage for review
        array_list = []
        while head != None :
            array_list.append(head.val)
            head = head.next 
        # Remove nth element from tail to head
        array_list.pop(len(array_list)-n)
        # Re-create the new linked list to return as solution
        if len(array_list) > 0 :
            index = len(array_list)-1
            # Tail element
            solution = ListNode(array_list[index])
            index -= 1
            head = solution
            # Rest of elements
            while index >= 0 :
                new_node = ListNode(array_list[index])
                new_node.next = solution
                solution = new_node
                index -= 1
        else :
            return None
        return solution

