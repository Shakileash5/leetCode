class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        size = len(digits)
        keyPad = {
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        res = []
        def getCombinations(idx,temp):
            if idx>=size:
                if temp!='':
                    res.append(temp)
                return
            
            for i in range(len(keyPad[digits[idx]])):
                getCombinations(idx+1,temp+keyPad[digits[idx]][i])
            return
        
        getCombinations(0,'')
        return res