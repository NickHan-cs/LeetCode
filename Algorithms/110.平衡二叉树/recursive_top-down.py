# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return abs(self.getDepth(root.left) - self.getDepth(root.right)) <= 1 and self.isBalanced(
            root.left) and self.isBalanced(root.right)

    def getDepth(self, root: TreeNode):
        if root is None:
            return 0
        return max(self.getDepth(root.left), self.getDepth(root.right)) + 1
