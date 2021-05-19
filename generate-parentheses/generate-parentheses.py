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
            
    def backtrackSolTwo(self,openBr,closeBr,n,subStr):
        if len(subStr) == (n*2):
            self.res.append(subStr)
            return
        else:
            if openBr<n:
                self.backtrackSolTwo(openBr+1,closeBr,n,subStr+"(")
            if closeBr<n and closeBr<openBr:
                #print("close",openBr,closeBr)
                self.backtrackSolTwo(openBr,closeBr+1,n,subStr+")")
                
        return
    
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        strn = [""] * 2 * n
        #if (n>0):
        #    self.backtrack(self.res,strn,0,0,0,n)
        #self._printParenthesis(strn, 0, n, 0, 0);
        self.backtrackSolTwo(0,0,n,"")
        return self.res