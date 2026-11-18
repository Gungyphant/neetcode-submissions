class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Create a matrix as wide as the input is tall, and as tall as the input is wide
        matrix_height = len(matrix)
        matrix_width = len(matrix[0])
        result = [[None for _ in range(matrix_height)] for _ in range(matrix_width)]

        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                result[x][y] = val
        return result
