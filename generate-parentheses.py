# https://leetcode.com/problems/generate-parentheses/
# Problem Description

# Solution
class Solution:
    def backtrack(self,res,strn,pos,o,c,n):
        if c== n:
            res.append("".join(strn))
            return
        else:
            if o>c:
                strn[pos]=")"
                self.backtrack(res,strn,pos+1,o,c+1,n)
            if o<n:
                strn[pos]="("
                self.backtrack(res,strn,pos+1,o+1,c,n)
            
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        strn = [""] * 2 * n
        if (n>0):
            self.backtrack(res,strn,0,0,0,n)
        #self._printParenthesis(strn, 0, n, 0, 0);
        return res