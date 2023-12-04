# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ouput = ListNode()
        carry = 0

        current_node = ouput
        while l1 or l2 or carry:
            current_l1_value = l1.val if l1 else 0
            current_l2_value = l2.val if l2 else 0
            carry, rest = divmod(current_l1_value + current_l2_value + carry, 10)

            l1 = l1.next if l1 and l1.next else None
            l2 = l2.next if l2 and l2.next else None

            current_node.next = ListNode(rest)
            current_node = current_node.next
        return ouput.next