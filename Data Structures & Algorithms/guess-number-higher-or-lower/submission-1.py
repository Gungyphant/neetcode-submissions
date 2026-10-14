# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lower = 1
        upper = n
        while lower < upper:
            my_guess = int((lower + upper) / 2)
            result = guess(my_guess)
            if result == 0:
                return my_guess
            elif result == -1:
                upper = my_guess - 1
            else:
                lower = my_guess + 1
        return lower
        