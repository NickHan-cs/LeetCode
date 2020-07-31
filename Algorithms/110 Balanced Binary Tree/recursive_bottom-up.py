# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalancedHelper(self, root: TreeNode):
        if root is None:
            return True, -1
        leftIsBalanced, leftDepth = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, 0
        rightIsBalanced, rightDepth = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, 0
        return abs(leftDepth - rightDepth) <= 1, 1 + max(leftDepth, rightDepth)

    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedHelper(root)[0]
