class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        sizeG = len(g)
        sizeS = len(s)
        res = 0
        idx = 0
        print(g,s)
        for i in range(sizeG):

            while idx<sizeS and g[i]>s[idx]:
                idx += 1
            if idx>=sizeS:
                break
            if g[i]<=s[idx]:            
                res += 1
                idx += 1
        
        return res
            