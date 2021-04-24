class Solution:
    def smallestSubsequence(self, s: str) -> str:
        size = len(s)
        idxMap = {}
        stack = []
        inStack = set()
        
        for i in range(size):
            idxMap[s[i]] = i
        
        for i in range(size):
            if s[i] not in inStack:
                
                while stack and s[i]<stack[-1] and idxMap[stack[-1]]>i:
                    inStack.remove(stack.pop())
                
                stack.append(s[i])
                inStack.add(s[i])
        
        #print(stack)
        
        return "".join(stack)