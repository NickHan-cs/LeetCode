# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        newHead = ListNode(0)
        newHead.next = head
        node = newHead
        while node.next and node.next.next:
            if node.next.val != node.next.next.val:
                node = node.next
            else:
                tmp = node.next.next
                while tmp.next and tmp.next.val == node.next.val:
                    tmp = tmp.next
                node.next = tmp.next
        return newHead.next
