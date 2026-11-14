import itertools
import math

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        result = 0
        tuple_t = tuple(t)
        set_s = set(s)
        set_t = set(t)
        if s[0] == t[0] and len(set_s) == 1 and len(set_t) == 1:
            return math.comb(len(s), len(t))
        elif any(c not in set_s for c in set_t):
            return 0
        for chars in itertools.combinations(s, len(t)):
            if chars == tuple_t:
                result += 1
        return result
