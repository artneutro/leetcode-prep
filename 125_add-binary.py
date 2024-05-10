# https://leetcode.com/problems/add-binary/
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = '0b' + a
        b = '0b' + b
        a_int = int(a, 2)
        b_int = int(b, 2)
        return str(bin(a_int+b_int))[2:]
        
