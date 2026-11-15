class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums.sort()
        for i in range(len(nums)):
            v_i = nums[i]
            for j in range(i + 1, len(nums)):
                v_j = nums[j]
                total = v_i + v_j
                if total == target:
                    print(v_i, v_j, total)
                    return [i, j]
                # elif total > target:
                    # break
        