import bisect

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = []
        curr = list1
        while curr is not None:
            bisect.insort(merged, curr.val)
            curr = curr.next

        curr = list2
        while curr is not None:
            bisect.insort(merged, curr.val)
            curr = curr.next

        new = ListNode()
        curr = new
        for x in merged:
            curr.next = ListNode(x)
            curr = curr.next
        
        return new.next
        