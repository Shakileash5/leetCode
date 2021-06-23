class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        size = len(num)
        stack = []
        
        if len(num) == k:
            return "0"
        if not k:
            return num
        
        for i in range(size):
            val = num[i]
            if(stack and k):
                while stack and k and val<stack[-1]:
                    val_ = stack.pop()
                    k -= 1
                    
            stack.append(val)
            if len(stack) == 1 and stack[-1] == '0':
                stack.pop()
        
        while(stack and k):
            stack.pop()
            k -= 1
        
        return "".join(stack) if stack else '0'