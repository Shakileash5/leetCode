class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        size = len(s)
        hashMap = {'a':-1,'b':-1,'c':-1}
        count = 0
        listIdx = [-1,-1,-1]
        n = 0
        for i, c in enumerate(s):
            hashMap[c] = i
            n += i - min(hashMap.values())
        return (1 + len(s)) * len(s) // 2 - n
        
        """for i in range(size):
            if s[i] in ['a','b','c']:
                if hashMap[s[i]] == -1:
                    hashMap[s[i]] = [i]
                else:
                    hashMap[s[i]].append(i)
        for key in ['a','b','c']:
            if hashMap[key] == -1:
                return 0
        for i in range(size):
            for j in range(i+1,size):
                subStr = s[i:j+1]
                flag = 0
                for key in ['a','b','c']:
                    for val in hashMap[key]:
                        if val>=i and val<=j:
                            flag +=1
                            break
                if flag==3:
                    count+=1"""
        return count