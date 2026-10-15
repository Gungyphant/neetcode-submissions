class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freqs = {k: arr.count(k) for k in arr}
        return max([k for k, v in freqs.items() if k == v], default=-1)