class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None
        left, right = self.sortList(head), self.sortList(mid)
        newHead = ListNode(0)
        tmp = newHead
        while left and right:
            if left.val < right.val:
                tmp.next, left = left, left.next
            else:
                tmp.next, right = right, right.next
            tmp = tmp.next
        if left:
            tmp.next = left
        else:
            tmp.next = right
        return newHead.next


inputList = [4, 2, 1, 3]
head = ListNode(inputList[0])
tmp = head
for i in range(1, len(inputList)):
    tmp.next = ListNode(inputList[i])
    tmp = tmp.next
sol = Solution()
newHead = sol.sortList(head)
while newHead:
    print(newHead.val, end=" ")
    newHead = newHead.next