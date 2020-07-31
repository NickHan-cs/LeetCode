# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        newHead = None
        while head:
            node = ListNode(head.val)
            node.next = newHead
            newHead = node
            head = head.next
        return newHead
