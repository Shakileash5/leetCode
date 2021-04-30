class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        s = '1['+s+']'
        size = len(s)
        i = 0
        while(i<size):
            strTil = i
            subStr = ""
            if s[i].isalpha():
                while(s[strTil].isalpha()):
                    subStr+=s[strTil]
                    strTil+=1
                stack.append(subStr)
            
            i = strTil
            
            numTil = i
            num = ""
            if s[i].isnumeric():
                while(s[numTil].isnumeric()):
                    num+=s[numTil]
                    numTil+=1
                #if numTil!=i:
                stack.append(int(num))
            
            i = numTil
            
            if s[i] == '[':
                stack.append('[')
                i+=1
            if s[i] == ']':
                idx = i
                res = []
                while(stack[-1]!='['):
                    res.append(stack.pop())
                res = "".join(res[::-1])
                stack.pop()
                stack.append(stack.pop()*res)
                #print(stack)
                i+=1
            
        #print(stack)
        return stack[-1]
                        
                        
                        
                    
                    