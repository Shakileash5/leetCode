class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        binary = bin(n)
        if str(binary).count('1') == 1 and n>0:
            return True
        return False