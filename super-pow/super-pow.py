class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if a in [1,0]:
            return a
        bigInt = int("".join(str(i) for i in b))
        res = int(pow(a,bigInt,1337))
        return res