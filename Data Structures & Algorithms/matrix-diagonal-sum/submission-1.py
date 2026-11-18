class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        for i in range(len(mat)):
            result += mat[i][i]
            j = len(mat) - 1 - i
            if j != i:
                result += mat[i][j]
        return result