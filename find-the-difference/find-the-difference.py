class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        size = len(s)
        
        for i in range(size):
            if s[i] != t[i]:
                return t[i]
        
        return t[-1]