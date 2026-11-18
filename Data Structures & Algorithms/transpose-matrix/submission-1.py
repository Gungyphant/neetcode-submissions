class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = [[None for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                result[x][y] =val
        return result
