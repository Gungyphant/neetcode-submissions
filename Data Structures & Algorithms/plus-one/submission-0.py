class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        if digits[-1] == 10:
            digits[-1] = 0
            for i, digit in list(enumerate(digits))[::-1][1:]:
                if digit == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    break
            else:
                digits = [1] + digits
        return digits
        