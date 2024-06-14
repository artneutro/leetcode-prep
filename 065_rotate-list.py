# https://leetcode.com/problems/rotate-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur_head = head
        list_items = []
        # Case []
        if k == 0 or head == None :
            return head
        while head != None :
            list_items.append(head.val)
            head = head.next
        # Case len == 1 
        if len(list_items) == 1 :
            return cur_head
        # Calculate how many full rotations k has and the remaining
        factor = k%len(list_items)
        # Perform the only rotation needed using this factor
        solution = list_items[len(list_items)-factor:] + list_items[:len(list_items)-factor]
        # Create the new LinkedList using the solution
        cur_head = ListNode(solution[0])
        head = cur_head
        index = 1
        while index < len(solution) :
            new_node = ListNode(solution[index])
            head.next = new_node
            head = head.next
            index += 1
        return cur_head

