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
        
        if depth % 2 == 0:
            self.result[depth].append(node.val)
        else:
            self.result[depth] = [node.val] + self.result[depth]

        self.traverse(node.left, depth + 1)
        self.traverse(node.right, depth + 1)

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = []
        self.traverse(root)
        return self.result        