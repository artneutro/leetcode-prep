# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Empty list case
        if head == None :
            return head
        # Variables initialization
        new_head = None
        cur_value = head.val
        iterator_next = head.next
        # This one is to check last not duplicated node
        duplicated = False
        # Iterate over the list and remove duplicated O(n) time and space
        while iterator_next != None :
            # If duplicated found, skip all of them
            if cur_value == iterator_next.val :
                duplicated = True
                while iterator_next != None and iterator_next.val == cur_value :
                    iterator_next = iterator_next.next
                if iterator_next != None :
                    cur_value = iterator_next.val
                    duplicated = False
            # If different element confirmed, then add to the final list
            else :
                # First node
                if new_head == None :
                    new_head = ListNode(cur_value)
                    head = new_head
                    cur_value = iterator_next.val
                # Non first nodes
                else :
                    new_node = ListNode(cur_value)
                    new_head.next = new_node
                    new_head = new_head.next
                    cur_value = iterator_next.val
            if iterator_next != None :
                iterator_next = iterator_next.next
            else : 
                break
        # Last node  
        if not duplicated and new_head == None :
            new_head = ListNode(cur_value)
            head = new_head
        elif not duplicated and new_head != None :
            new_node = ListNode(cur_value)
            new_head.next = new_node    
        # [1, 1]
        if duplicated and new_head == None :   
            head = new_head  
        return head

