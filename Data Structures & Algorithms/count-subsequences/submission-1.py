import itertools

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        result = 0
        for length in range(len(s) + 1):
            for chars in itertools.combinations(s, length):
                if "".join(chars) == t:
                    result += 1
        return result
