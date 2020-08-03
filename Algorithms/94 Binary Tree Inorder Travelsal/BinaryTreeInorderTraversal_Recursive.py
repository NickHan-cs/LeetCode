# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        nodeList = self.Recursive(root)
        valList = []
        for i in nodeList:
            valList.append(i.val)
        return valList


    def Recursive(self, root):
        if not root:
            return []
        return self.Recursive(root.left) + [root] + self.Recursive(root.right)
