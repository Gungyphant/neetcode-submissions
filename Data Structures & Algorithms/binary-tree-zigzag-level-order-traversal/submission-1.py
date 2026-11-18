# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = []
    def traverse(self, node, depth=0):
        if node is None: return
        while depth >= len(self.result):
            self.result.append([])
        self.result[depth].append(node.val)

        self.traverse(node.left, depth + 1)
        self.traverse(node.right, depth + 1)

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = []
        self.traverse(root)
        for i in range(1, len(self.result), 2):
            self.result[i] = self.result[i][::-1]
        return self.result        