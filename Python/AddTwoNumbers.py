# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # result = ListNode(0)
        result = ListNode(l1.val + l2.val)
        if (l1.next != none | | l2.next != none):
            l3 = l1.next
        result.next = ListNode(l3.val + l2.next.val)
        result.next.next = ListNode(l1.next.next.val + l2.next.next.val)

        return result