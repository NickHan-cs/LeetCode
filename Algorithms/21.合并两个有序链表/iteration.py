# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            head, l1 = l1, l1.next
        else:
            head, l2 = l2, l2.next
        tmp = head
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                tmp, l1 = tmp.next, l1.next
            else:
                tmp.next = l2
                tmp, l2 = tmp.next, l2.next
        if l1:
            tmp.next = l1
        else:
            tmp.next = l2
        return head
