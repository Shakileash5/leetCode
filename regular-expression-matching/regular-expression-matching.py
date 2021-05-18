class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # p = letter | letter * | . | .*
        sizeStr = len(s)
        sizePattern = len(p)
        
        def backtrack(idxStr,idxPattern):
            if idxPattern>=sizePattern or idxStr>=(sizeStr):
                print(idxStr,idxPattern,"end")
                if idxPattern>=sizePattern and idxStr>=(sizeStr):
                    return True
                if idxPattern>=idxStr and idxStr>=sizeStr:

                    if idxPattern+1 == (sizePattern-1) and p[idxPattern+1]=='*':
                        return True
                return False
            
            if p[idxPattern]!= '*' and p[idxPattern]!= '.':
                print("atleast",idxStr,idxPattern,sizeStr,sizePattern)
                if idxPattern+1<sizePattern and p[idxPattern+1] == '*':
                    print("didImakeit")
                    return backtrack(idxStr,idxPattern+1)
                else:   
                    if p[idxPattern] != s[idxStr]:
                            print(idxStr,idxPattern,"omg killed")
                            return False
                    return backtrack(idxStr+1,idxPattern+1)
            else:
                if p[idxPattern] == '.':
                    #print(idxStr,idxPattern,"for dot")
                    return backtrack(idxStr+1,idxPattern+1)
                elif p[idxPattern] == '*':
                    if p[idxPattern-1]!='.':
                        if p[idxPattern-1] == s[idxStr]:
                            return backtrack(idxStr+1,idxPattern) or backtrack(idxStr+1,idxPattern+1)
                        else:
                            return backtrack(idxStr,idxPattern+1)
                    return backtrack(idxStr+1,idxPattern) or backtrack(idxStr+1,idxPattern+1)
        sn = len(s)
        pn = len(p)
        def matchedAt(si, pi):
            if pi == pn:
                return si == sn
            ch_matched = si < sn and (p[pi] == '.' or p[pi] == s[si]) 
            if pi + 1 < pn and p[pi + 1] == '*':
                return (matchedAt(si, pi + 2) or
                        ch_matched and matchedAt(si + 1, pi))
            else:
                return ch_matched and matchedAt(si + 1, pi + 1)
        #return backtrack(0,0) 
        return matchedAt(0, 0)
    
        