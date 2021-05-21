class Solution:
    def checkChar(self, s, p, s_i, p_i) -> bool:
        if p_i >= len(p):
            return s_i >= len(s)
        else:
            if s_i >= len(s):
                return functools.reduce(lambda x,y: x and y, (c=='*' for c in p[p_i:]))
            elif self.memo[s_i][p_i] is None:
                if p[p_i] == '*':
                    self.memo[s_i][p_i] = (self.checkChar(s,p,s_i,p_i+1) or self.checkChar(s,p,s_i+1,p_i))
                else:
                    if p[p_i] != '?' and s[s_i] != p[p_i]:
                        self.memo[s_i][p_i] = False
                    else:
                        self.memo[s_i][p_i] = self.checkChar(s,p,s_i+1,p_i+1)
            return self.memo[s_i][p_i]
    def recur(self,p,s,idxS,idxP):
        if idxP == len(p):
            if idxS >= len(s):
                #print("here2")
                return True
            else:
                return False
        if idxS == len(s):
            #print("here")
            if idxP == len(p)-1 and p[idxP] == "*":
                return True
            if idxP == len(p):
                return True
            return False
        if p[idxP] != '*' and p[idxP] != '?':
            if s[idxS] == p[idxP]:
                return self.recur(p,s,idxS+1,idxP+1)
            #print("ic")
            return False
        else:
            if p[idxP] == "?":
                return self.recur(p,s,idxS+1,idxP+1)
            elif p[idxP]=="*":
                sol = False
                if idxP == len(p)-1:
                    if self.recur(p,s,idxS+1,idxP):
                        return True
                    if self.recur(p,s,idxS+1,idxP+1):
                        return True
                else:
                    if s[idxS] == p[idxP+1]:
                        if self.recur(p,s,idxS,idxP+1):
                            return True
                        if self.recur(p,s,idxS+1,idxP):
                            return True
                    else:
                        if self.recur(p,s,idxS,idxP+1):
                            return True
                        if self.recur(p,s,idxS+1,idxP):
                            return True
        return False
    
    
    
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0:
            if len(p) == 0:
                return True
            for i in range(len(p)):
                if p[i]!="*":
                    return False
            return True
        
        #return (self.recur(p,s,0,0))
        self.memo = [[None for p_i in range(len(p))] for s_i in range(len(s))]
        return self.checkChar(s,p,0,0)