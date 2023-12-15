from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer_list = deque([])
        
        curr = head
        while curr is not None:
            pointer_list.appendleft(curr)
            curr = curr.next

        if len(pointer_list) == 1:
            return None

        if len(pointer_list) == n:
            return head.next
        selected = pointer_list[n]
        selected.next = selected.next.next if selected.next is not None else None
        return head
        