import itertools

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if all(n == 0 for n in nums):
            a, b = divmod(len(nums), 3)
            if b == 0:
                return a
            else:
                return -1
        nums = [1 if n else -1 for n in nums]
        for number_flipped in range(len(nums)):
            for flip_indices in itertools.combinations(range(1, len(nums) - 1), number_flipped):
                local_nums = nums.copy()
                for i in flip_indices:
                    local_nums[i - 1] *= -1
                    local_nums[i] *= -1
                    local_nums[i + 1] *= -1
                if all(n == 1 for n in local_nums):
                    return number_flipped
        return -1
