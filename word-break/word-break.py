class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        sizeDict = len(wordDict)
        sizeStr = len(s)
        dp = [None for i in range(sizeStr+1)]
        
        def recur(idx):
            if idx>=sizeStr:
                return True
            
            if dp[idx] == None:
                for i in range(idx,sizeStr):
                    subStr = s[idx:i+1]
                    if subStr in wordDict:
                        if recur(i+1):
                            return True
            dp[idx] = False
            return False
        
        return recur(0)
                