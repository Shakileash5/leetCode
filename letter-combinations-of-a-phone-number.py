# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Problem Description

# Solution
def backTrack(res,comd,digit,index,letterFormat):
        if len(digit) == index:
            res.append(comd)
            return
        else:
            for i in letterFormat[digit[index]]:
                comd +=i
                backTrack(res,comd,digit,index+1,letterFormat)
                comd = comd[:-1]
    
class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        
        letterFormat = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        if digits == "":
            return []
        res = []
        backTrack(res,"",digits,0,letterFormat)
        return res
        