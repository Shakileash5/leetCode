class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        size = len(s)
        stack = []
        strStack = []
        start = 0
        res =  ''
        
        for i in range(size):
            if stack:
                if s[i] == ")":
                    stack.pop()
                if stack == []:
                    strStack.append(s[start:i+1])
                    start = i + 1
            if s[i] == "(":
                stack.append(s[i])
        
        for item in strStack:
            res += item[1:-1]
        return res