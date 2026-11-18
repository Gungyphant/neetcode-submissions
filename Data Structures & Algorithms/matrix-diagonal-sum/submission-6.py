class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # result = 0
        # for i in range(len(mat)):
        #     result += mat[i][i]
        #     j = len(mat) - 1 - i
        #     if j != i:
        #         result += mat[i][j]
        # return result
        size = len(mat)
        return sum(mat[i][i] + (mat[i][j] if j != i else 0) for i, j in ((i, size - 1 - i) for i in range(size)))