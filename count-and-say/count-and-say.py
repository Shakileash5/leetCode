class Solution:
    def recur(self,n,say):
        if say == 1:
            return n
        count = 1
        nStr = str(n)
        size = len(nStr)
        res = ""
        #print("say",say,n)
        if size==1:
            res = str(count)+nStr[0]
            #print("entered size 1")
            return self.recur(res,say-1)
        
        for i in range(1,size):
            #print("in for ith",i)
            if nStr[i-1] == nStr[i]:
                count+=1
            else:
                res+= str(count)+nStr[i-1]
                count = 1
            #print(count)
        res = res + str(count)+nStr[-1]
        return self.recur(res,say-1)
    
    def recurTwo(self,string,say):
        if say == 1:
            return string
        
        size = len(string)
        idx = size-1
        count = 1
        resStr = ""
        #print(say,string)
        while(idx>=0):
            tempIdx  = idx
            while (idx-1)>=0 and string[idx] == string[idx-1]:
                idx-=1
                count+=1
                #print("here")
            resStr = str(count) + string[tempIdx] + resStr
            idx-=1
            count = 1
            #print("run",idx)
        #print(resStr)
        return self.recurTwo(resStr,say-1)
        
    
    
    def countAndSay(self, n: int) -> str:
        
        if n == 1:
            return "1"
        
        #res = self.recur("1",n)
        #print()
        #return res
        return self.recurTwo("1",n)
        
        
        