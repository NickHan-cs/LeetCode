# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        preNode, curNode = None, head
        for i in range(m - 1):
            preNode, curNode = curNode, curNode.next
        newHead, end = preNode, curNode
        for i in range(m, n + 1):
            curNode.next, preNode, curNode = preNode, curNode, curNode.next
        if newHead:
            newHead.next = preNode
        else:
            head = preNode
        end.next = curNode
        return head
