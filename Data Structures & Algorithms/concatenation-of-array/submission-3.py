class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for n in nums[:len(nums)]:
            nums.append(n)
        return nums