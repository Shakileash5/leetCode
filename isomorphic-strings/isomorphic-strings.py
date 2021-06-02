class Solution:
    def isIsomorphicTwo(self,s,t):
        hashMapS = {}
        hashMapT = {}
        size = len(s)
        
        for i in range(size):
            flag = -1
            if s[i] in hashMapS:
                flag = hashMapS[s[i]]
                hashMapS[s[i]] = i
            else:
                hashMapS[s[i]] = i
            if flag == -1:
                if t[i] in hashMapT:
                    return False
                hashMapT[t[i]] = i
            else:
                if t[i] not in hashMapT:
                    return False
                if hashMapT[t[i]] != flag:
                    return False
                hashMapT[t[i]] = i
        
        return True
                
        
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        def solutionOne():
            hashMapS = {}
            hashMapT = {}
        
            for i in range(len(s)):
                flag = 0
                if t[i] not in hashMapT:
                    hashMapT[t[i]] = [j for j, x in enumerate(t) if x == t[i]]
                    #print(hashMapT,t[i])
                    if s[i] not in hashMapS:
                        hashMapS[s[i]] = [k for k, x in enumerate(s) if x == s[i]]
                        #print(hashMapS,s[i])
                        if hashMapT[t[i]] != hashMapS[s[i]]:
                            return False
                    else:
                        return False
                else:
                    if s[i] not in hashMapS:
                        return False

            return True
        
        return self.isIsomorphicTwo(s,t)