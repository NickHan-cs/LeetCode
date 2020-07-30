from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
class Solution:
    def __init__(self):
        self.ans = []

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def getNextLevelOrder(lastlevel):
            if len(lastlevel) == 0:
                return
            nextLevelNode = []
            nextLevelVal = []
            for node in lastlevel:
                if not node.left:
                    nextLevelNode.append(node.left)
                    nextLevelVal.append(node.left.val)
                if not node.right:
                    nextLevelNode.append(node.right)
                    nextLevelVal.append(node.right.val)
            if len(nextLevelVal) > 0:
                self.ans.append(nextLevelVal[:])
            getNextLevelOrder(nextLevelNode)

        self.ans = [[root.val]]
        getNextLevelOrder([root])
        return self.ans
'''


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        level = [root]
        while len(level) > 0:
            nextLevel = []
            val = []
            for node in level:
                val.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            ans.append(val[:])
            level = nextLevel[:]
        return ans


treeVal = [3, 9, 20, None, None, 15, 7]
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
print(sol.levelOrder(treeNode[0]))
