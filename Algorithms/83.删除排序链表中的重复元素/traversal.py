# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tmp = head
        while tmp and tmp.next:
            if tmp.val == tmp.next.val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return head
