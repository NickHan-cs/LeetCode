# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def getNodePathSum(node):
            if node is None:
                return 0
            leftPathSum = max(getNodePathSum(node.left), 0)
            rightPathSum = max(getNodePathSum(node.right), 0)
            nodePathSum = node.val + leftPathSum + rightPathSum
            self.maxSum = max(self.maxSum, nodePathSum)
            return node.val + max(leftPathSum, rightPathSum)

        getNodePathSum(root)
        return self.maxSum
