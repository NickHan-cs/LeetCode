class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return False
            leftNodeFlag = dfs(node.left)
            rightNodeFlag = dfs(node.right)
            if leftNodeFlag and rightNodeFlag or (leftNodeFlag or rightNodeFlag) and (
                    node.val == p.val or node.val == q.val):
                self.ans = node
            return node.val == p.val or node.val == q.val or leftNodeFlag or rightNodeFlag

        dfs(root)
        return self.ans
