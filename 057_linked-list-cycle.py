# https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # List of visited nodes
        visited = []
        while (head) : 
            # Store the object address (not the value), as there could be repeated values
            visited.append(id(head)) 
            if head.next : 
                if id(head.next) in visited :
                    return True
            head = head.next 
        return False

