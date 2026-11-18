import numpy

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return numpy.matrix(matrix).T.tolist()
        
