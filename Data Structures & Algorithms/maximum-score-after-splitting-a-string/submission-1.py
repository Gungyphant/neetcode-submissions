class Solution:
    def maxScore(self, s: str) -> int:
        result = 0
        for split in range(1, len(s)):
            left = s[:split]
            right = s[split:]
            score = left.count("0") + right.count("1")
            if score > result:
                # print(split, left, right, score)
                result = score
        return result