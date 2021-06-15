class Solution:
    def decodeString(self, s: str) -> str:
        size = len(s)
        stack = []
        idx = 0 
        res = ''
        
        while idx<size:
            if s[idx].isnumeric():
                strInt = ''
                while s[idx] != '[':
                    strInt = strInt + s[idx]
                    idx += 1
                stack.append(int(strInt))
                continue
            elif s[idx] == '[':
                stack.append(s[idx])
            elif s[idx] == ']':
                #print(stack,"here")
                str_ = ''
                while(stack!=[] and stack[-1]!='['):
                    str_ = stack.pop() + str_ 
                #print(str_)
                stack.pop()
                val = stack.pop()
                stack.append(val*str_)
            else:
                if stack == [] or stack[-1]=='[':
                    stack.append(s[idx])
                else:
                    stack[-1] += s[idx] 
            #print(stack)
            idx += 1 
        return ''.join(stack)