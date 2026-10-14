class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = set()
        for n in range(2 ** len(nums)):
            bin_n = bin(n)[2:].zfill(len(nums))
            print(n, bin_n)
            results.add(tuple(sorted([nums[i] for i in range(len(nums)) if bin_n[i] == "1"])))
        return list(results)
        