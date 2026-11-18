# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
sys.setrecursionlimit(1000000000)
class Solution:
    # def sum(self, node):
    #     if node is None: return 0
    #     return self.sum(node.left) + node.val + self.sum(node.right)

    def convert(self, node):
        if node is None: return None
        # print(node.val, self.sum(node.right))
        return TreeNode(node.val + sum(n for n in self.vals if n > node.val), self.convert(node.left), self.convert(node.right))

    vals = []

    def load_vals(self, start_node):
        nodes = [start_node]
        while nodes:
            node = nodes.pop(0)
            if node is None: continue
            self.vals.append(node.val)
            nodes.append(node.left)
            nodes.append(node.right)

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.vals = []
        self.load_vals(root)
        # print(self.vals)
        return self.convert(root)
        