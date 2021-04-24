class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        size = len(s)
        sortedS = sorted(list(set(s)))
        res = []
        lastIdx = {char: indx for indx, char in enumerate(s)}
        #print(lastIdx)
        visited = set()
        
        for i,val in enumerate(s):
            if val not in visited:
                while res and val<res[-1] and i<lastIdx[res[-1]]:
                    visited.remove(res.pop())
                res.append(val)
                visited.add(val)
        #print(res,"here")
        string = "".join(res)
        
        def recur(idx,temp):
            if idx>=(size-1):
                if sorted(temp) == sortedS:
                    if temp not in res:
                        res.append(temp)
                return
            for i in range(idx+1,size):
                recur(i,temp+s[i])
                recur(i,temp)
        
        #recur(-1,'')
        #print(res)
        #print(min(res))
        return string