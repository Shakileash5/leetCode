class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        
        
        arr = preorder.split(",")
        size = len(arr)
        #print(size)
        def verifyPreorder(arr): 
            stack = []
            for i in arr:
                stack.append(i)
                while len(stack)>=3:
                    if stack[-1] == '#' and stack[-2] == '#' and stack[-3] != '#':
                        stack.pop()
                        stack.pop()
                        stack[-1] = '#'
                    else:
                        break
                
            if len(stack)>1 or stack[-1] != "#":
                return False
            return True
                
        
        return verifyPreorder(arr)