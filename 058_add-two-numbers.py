# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ''
        n2 = ''
        # Get number 1 from linked-list 1
        while (l1 != None) :
            n1 += str(l1.val)
            l1 = l1.next
        # Get number 2 from linked-list 2
        while (l2 != None) :
            n2 += str(l2.val)
            l2 = l2.next
        # Reverse both numbers (as strings)
        n1 = n1[::-1]
        n2 = n2[::-1]
        # Sum up both numbers (as integers)
        result = str(int(n1) + int(n2))
        index = 0
        output = None
        # Create the result linked-list
        while (index < len(result)) :
            # Rest of nodes
            if output != None :
                new_output = ListNode(result[index])
                new_output.next = output
                output = new_output
            # First node
            else :
                output = ListNode(result[index])
            index += 1
        return output

