from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.pre = float("-inf")
        self.flag = True

    def isValidBST(self, root: TreeNode) -> bool:
        def inOrder(node):
            if not node or not self.flag:
                return
            inOrder(node.left)
            if node.val <= self.pre:
                self.flag = False
                return
            self.pre = node.val
            inOrder(node.right)

        inOrder(root)
        return self.flag


treeVal = [5, 1, 4, None, None, 3, 6]
treeNode = []
for i in treeVal:
    if i:
        treeNode.append(TreeNode(i))
    else:
        treeNode.append(None)
l = len(treeNode)
for i in range(l):
    if 2 * i + 2 > l:
        break
    treeNode[i].left = treeNode[2 * i + 1]
    treeNode[i].right = treeNode[2 * i + 2]
sol = Solution()
print(sol.isValidBST(treeNode[0]))
