from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new = ListNode(next=head)
        initial_current = new
        while initial_current.next is not None:
            count = 0
            curr = initial_current
            temp = deque([])
            while count < k and curr.next is not None:
                temp.appendleft(curr.next)
                curr = curr.next
                count += 1

            curr = initial_current
            if len(temp) == k:
                last = temp[0].next
                for x in temp:
                    curr.next = x
                    curr = x
                curr.next = last
                initial_current = curr
            else:
                break
        return new.next      