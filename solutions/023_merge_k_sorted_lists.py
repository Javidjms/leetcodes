import bisect

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = []
        for curr in lists:
            while curr is not None:
                bisect.insort(merged, curr.val)
                curr = curr.next

        new = ListNode()
        curr = new
        for x in merged:
            curr.next = ListNode(x)
            curr = curr.next
        
        return new.next 