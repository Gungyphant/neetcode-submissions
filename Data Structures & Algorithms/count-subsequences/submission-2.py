import itertools

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        result = 0
        tuple_t = tuple(t)
        for length in range(len(s) + 1):
            for chars in itertools.combinations(s, length):
                if chars == tuple_t:
                    result += 1
        return result
