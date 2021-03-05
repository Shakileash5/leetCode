# https://leetcode.com/problems/valid-parentheses/
# Problem Description

# Solution
class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        closingType = list(brackets.keys())
        stack = []
        size = len(s) 
        for i in range(size):
            #print(stack)
            if s[i] in closingType:
                if len(stack) > 0:
                    last = stack.pop()
                else:
                    return False
                #print("w",last,stack)
                if  last != brackets[s[i]]: 
                    #print("here")
                    return False
            else:
                stack.append(s[i])
        #print(stack)
        if len(stack)>0:
            return False
        return True
            