class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        size = len(s)
        stack = []
        count = 0
        res = ''
        for i in range(size):
            if s[i] == '(':
                stack.append('(')
                res += '('
            elif s[i] == ')':
                if stack:
                    stack.pop()
                    res += ')'
                
            else:
                res += s[i]
        idx = len(res)-1
        #print(res,stack)
        while(len(stack)):
            #print(res,idx)
            if res[idx] == '(':
                stack.pop()
                res = res[:idx]+res[idx+1:]
            
            idx -= 1
        
        return res