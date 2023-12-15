# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode(next=head)
        curr = new
        while curr.next is not None:
            if curr.next.next is not None:
                first = curr.next.next
                second = curr.next
                third = curr.next.next.next
                curr.next = first
                first.next = second
                second.next = third
                curr = second
            else:
                curr = curr.next
        return new.next
        