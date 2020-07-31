from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
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
            ans.insert(0, val[:])
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
print(sol.levelOrderBottom(treeNode[0]))
