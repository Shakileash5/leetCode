class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        size = len(arr)
        stack = [arr[-1]]
        res = []
        
        for i in range(size-2,-1,-1):
            if stack[-1]>arr[i]:
                stack.append(stack[-1])
            else:
                stack.append(arr[i])
        stack.pop()
        stack = stack[::-1]
        stack.append(-1)
        return stack