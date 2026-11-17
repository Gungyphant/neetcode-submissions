class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        differences = 0
        s1_count = defaultdict(int)
        s2_count = defaultdict(int)
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                differences += 1
                if differences > 2:
                    return False  # If more than 2 characters differ, it can't be correct
            s1_count[c1] += 1
            s2_count[c2] += 1
        if s1_count != s2_count: return False  # If the strings don't have the same number of each character, it's impossible to make s2
        print(differences)
        return differences != 1  # It's only possible if there are 0 or 2 differences
