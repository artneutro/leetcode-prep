# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Count the nodes to get final tail behaviour (still O(n) in time)
        index = head
        count = 0
        while index != None :
            count += 1
            index = index.next
        quotient = int(count/k)
        remainde = count%k
        # Iteratively reverse nodes with factor k up to quotient + remainder
        # Iteration 1
        prev_tail = None
        curr_head = head
        curr_iter = None
        curr_tail = head
        index_iter = 0
        while index_iter < k :
            head = head.next
            curr_head.next = curr_iter
            curr_iter = curr_head
            curr_head = head
            index_iter += 1
        # solution will contain the first reversed head
        solution = curr_iter
        prev_tail = curr_tail
        quotient -= 1
        # Iteration rests
        while quotient > 0 :
            curr_head = head
            curr_iter = None
            curr_tail = head
            # Iterate until k
            index_iter = 0
            while index_iter < k :
                head = head.next
                curr_head.next = curr_iter
                curr_iter = curr_head
                curr_head = head
                index_iter += 1
            # Attach prev_tail to curr_iter
            prev_tail.next = curr_iter
            # prev_tail = curr_tail
            prev_tail = curr_tail
            # Another segment have been reversed
            quotient -= 1
        if remainde > 0 :
            curr_tail.next = head
        # O(1) in space
        return solution

