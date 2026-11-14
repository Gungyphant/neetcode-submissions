class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        for c in s:
            if c not in t: return False
            t.remove(c)
        return not t
        