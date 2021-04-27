class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        size = len(s)
        start = 0
        end = size-1
        
        while(start<end):
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start+=1
            end-=1
        
        return