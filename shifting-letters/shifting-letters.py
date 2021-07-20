class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        size = len(s)
        res = list(s)
        sum_ = 0
        prefixShifts = []
        for val in shifts[::-1]:
            sum_ += val
            prefixShifts.append(sum_)
        prefixShifts = prefixShifts[::-1]
        
        for i in range(size):
            val = (ord(res[i])-ord('a')+prefixShifts[i])%26
            res[i] = chr(val+ord('a'))
        
        return ''.join(res)