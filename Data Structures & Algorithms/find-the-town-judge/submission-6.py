class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        possible_judges = list(range(1, n + 1))
        trustings = defaultdict(list)  # trustee: trusters
        for truster, trustee in trust:
            if truster in possible_judges:
                possible_judges.remove(truster)
            trustings[trustee].append(truster)
        return next((j for j in possible_judges if len(trustings[j]) == (n - 1)), -1)