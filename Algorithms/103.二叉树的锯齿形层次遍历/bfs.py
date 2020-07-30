from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        level = [root]
        i = 0
        while len(level) > 0:
            nextLevel = []
            val = []
            for node in level:
                val.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if i % 2 == 1:
                val.reverse()
            i += 1
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
print(sol.zigzagLevelOrder(treeNode[0]))