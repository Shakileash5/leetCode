class Solution:
    def numDecodings(self, s: str) -> int:
        
        @cache
        def recur(strn):
            if not strn:
                return 1
            
            else:
                ways = 0
                if 1<=int(strn[:1])<=26:
                    ways = recur(strn[1:])
                    if 1<=int(strn[:2]) and 26>=int(strn[:2]) and len(strn) > 1:
                        ways+=recur(strn[2:])

                return ways
        res = recur(s)
        return res
                
            
        