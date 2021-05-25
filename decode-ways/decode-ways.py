class Solution:
    
    def recur(self,idx,s):
        if idx>=len(s):
            #print("here")
            return 1
        
        way2 = 0
        way1 = 0
        if self.dp[idx] == None:
            if s[idx] != '0':
                way1 = self.recur(idx+1,s)
            if idx+1<len(s) and s[idx]!='0' and int(s[idx]+s[idx+1])<=26:
                way2 = self.recur(idx+2,s)
            self.dp[idx] = way1 + way2
            return self.dp[idx]
        else:
            return self.dp[idx]
    
    
    def numDecodings(self, s: str) -> int:
        
        def recur(strn,i,dp):
            
            if i>=len(strn):
                return 1
            if strn[i] == '0':
                return 0
            if dp[i]!=None:
                return dp[i]
            
            ways = recur(strn,i+1,dp)
            
            if (i+2)<=len(strn) and 1<=int(strn[i:i+2])<=26 :
                ways+= recur(strn,i+2,dp)
            
            dp[i] = ways
            return dp[i]
        
        dp = [None]*len(s)
        res = 0
        #res = recur(s,0,dp)
        #return res
        self.dp = [None]*len(s)
        return self.recur(0,s)
            
        