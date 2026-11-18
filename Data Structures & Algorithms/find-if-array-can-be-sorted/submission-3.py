from functools import cache

@cache
def sum_of_ones(n):
    return bin(n).count("1")

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        if len(set(nums)) == 1: return True
        did_swap = True
        while did_swap:
            did_swap = False
            for (i1, n1), (i2, n2) in zip(enumerate(nums), list(enumerate(nums))[1:]):
                if n1 > n2:
                    if sum_of_ones(n1) != sum_of_ones(n2):
                        return False
                    nums[i1] = n2
                    nums[i2] = n1
                    did_swap = True
                    break
                    
        return True
