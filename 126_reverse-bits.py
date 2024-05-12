# https://leetcode.com/problems/reverse-bits/
class Solution:
    def reverseBits(self, n: int) -> int:
        # Convert to binary 
        # Convert to string
        # Remove the '0b' part
        # Fill with leading '0' up to 32 bits
        # Reverse
        # Convert back to int
        return int((str(bin(n))[2:]).zfill(32)[::-1], 2)

