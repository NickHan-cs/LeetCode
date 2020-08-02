class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid, slow.next = slow.next, None
        preNode, curNode = None, mid
        while curNode:
            curNode.next, curNode, preNode = preNode, curNode.next, curNode
        while preNode:
            if preNode.val != head.val:
                return False
            preNode, head = preNode.next, head.next
        return True


inputList = [1, 2, 3, 4, 2, 1]
head = ListNode(inputList[0])
tmp = head
for i in range(1, len(inputList)):
    tmp.next = ListNode(inputList[i])
    tmp = tmp.next
sol = Solution()
print(sol.isPalindrome(head))
