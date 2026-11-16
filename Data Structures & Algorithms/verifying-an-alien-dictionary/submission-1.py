from functools import cache
from itertools import zip_longest


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        class word(str):
            def __lt__(self, other):
                for c1, c2 in zip_longest(self, other, fillvalue=""):
                    if order.index(c1) < order.index(c2):
                        return True
                    elif order.index(c1) > order.index(c2):
                        return False
                return False

        words = [word(w) for w in words]
        return words == sorted(words)