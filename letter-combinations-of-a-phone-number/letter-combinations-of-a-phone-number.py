'''def backTrack(res,comd,digit,index,letterFormat):
        if len(digit) == index:
            res.append(comd)
            return
        else:
            for i in letterFormat[digit[index]]:
                comd +=i
                backTrack(res,comd,digit,index+1,letterFormat)
                comd = comd[:-1]'''
    
class Solution:
    def backtrackSol2(self,letterFormat,idx,subStr,digits):
        if idx>=len(digits):
            if subStr not in self.result:
                self.result.append(subStr)
            return
        
        for i in range(len(letterFormat[digits[idx]])):
            self.backtrackSol2(letterFormat,idx+1,subStr+letterFormat[digits[idx]][i],digits)
        return
    
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
        self.result = []
        #backTrack(res,"",digits,0,letterFormat)
        self.backtrackSol2(letterFormat,0,"",digits)
        #print()
        return self.result
        