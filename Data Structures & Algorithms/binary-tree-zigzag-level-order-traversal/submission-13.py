# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = []
    result_pointers = []
    def traverse(self, node, depth=0):
        if node is None: return
        len_self_result = len(self.result)
        while depth >= len_self_result:
            size = 2 ** len_self_result
            self.result.append([None for _ in range(size)])
            self.result_pointers.append(0 if len_self_result % 2 == 0 else size - 1)

            len_self_result = len(self.result)
        
        self.result[depth][self.result_pointers[depth]] = node.val
        self.result_pointers[depth] += 1 if depth % 2 == 0 else -1

        self.traverse(node.left, depth + 1)
        self.traverse(node.right, depth + 1)

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = []
        self.result_pointers = []
        self.traverse(root)
        clean_result = []
        len_self_result = len(self.result)
        for i in range(0, len_self_result, 2):
            row = []
            for val in self.result[i]:
                if val is None:
                    break
                row.append(val)
            clean_result.append(row)

            if i + 1 == len_self_result:
                break
            
            row = []
            for j, val in enumerate(self.result[i + 1]):
                if val is not None:
                    row = self.result[i + 1][j:]
                    break
            clean_result.append(row)
        return clean_result
