class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        size = len(S)
        res = [S]

        def backtrack(idx,temp):
            #print(temp)
            if len(temp)==size:
                #print(temp)
                if temp not in res:
                    res.append(temp)
                return
            
            for i in range(idx,size):
                if S[i].isalpha():
                    if S[i].islower():
                        #print("were")
                        backtrack(i+1,temp+S[i].upper())
                        #print("backed")
                        backtrack(i+1,temp+S[i])
                    else:
                        #print("here")
                        backtrack(i+1,temp+S[i].lower())
                        backtrack(i+1,temp+S[i])
                else:
                    backtrack(i+1,temp+S[i])
            return
        
        backtrack(0,'')
        return res
                    
                    