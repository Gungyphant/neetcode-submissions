class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)
        result = [None for _ in range(2 * len(nums))]
        for i, n in enumerate(nums):
            result[i] = n
            result[i + l] = n
        return result