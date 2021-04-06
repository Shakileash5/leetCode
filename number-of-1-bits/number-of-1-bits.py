class Solution:
    def hammingWeight(self, n: int) -> int:
        #print(bin(n))
        bits = list(str(bin(n)))
        #print(bits)
        return bits.count('1')