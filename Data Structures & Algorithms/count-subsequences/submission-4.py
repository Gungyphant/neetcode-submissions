import itertools

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        result = 0
        tuple_t = tuple(t)
        for chars in itertools.combinations(s, len(t)):
            if chars == tuple_t:
                result += 1
        return result
