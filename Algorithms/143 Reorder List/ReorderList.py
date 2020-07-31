# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid, slow.next = slow.next, None
        preNode, curNode = None, mid
        while curNode:
            curNode.next, preNode, curNode = preNode, curNode, curNode.next
        tmp = head
        while preNode:
            tmp.next, preNode.next, tmp, preNode = preNode, tmp.next, tmp.next, preNode.next
