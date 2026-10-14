class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = sorted(set(nums))
        print(unique_nums)
        if not unique_nums:
            return 0
        prev_num = unique_nums[0]
        best_length = length = 1
        for n in unique_nums[1:]:
            if n == prev_num + 1:
                length += 1
            else:
                if length > best_length:
                    best_length = length
                length = 1
            prev_num = n
        if length > best_length:
            best_length = length
        return best_length
        