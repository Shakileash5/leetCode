class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMapS = {}
        hashMapT = {}
        
        '''for i in range(len(s)):
            print(s[i],t[i],s[i] != t[i])
            if s[i] != t[i]:
                print(s[i],t[i],"notmat",hashMap)
                if t[i] not in hashMap:
                    print(t[i],"not in")
                    hashMap[t[i]] = 1
                    s = s.replace(s[i],t[i])
                else:
                    return False
            hashMap[s[i]] = 1
            print(s,t,"\n")
        if s != t:
            return False'''
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