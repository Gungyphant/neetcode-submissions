class Solution:
    def reverseBits(self, n: int) -> int:
        str_n = bin(n)[2:].zfill(32)
        return int(str_n[::-1], 2)
        