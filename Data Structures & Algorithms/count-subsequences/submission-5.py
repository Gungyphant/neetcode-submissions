import itertools
import math

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        result = 0
        tuple_t = tuple(t)
        if s[0] == t[0] and len(set(s)) == 1 and len(set(t)) == 1:
            return math.comb(len(s), len(t))
        for chars in itertools.combinations(s, len(t)):
            if chars == tuple_t:
                result += 1
        return result
