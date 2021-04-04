class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def repeatingPattern(string):
            size = len(string)
            
            
            for i in range(1,size):
                    pattern = string[:i]
                    total = size//len(pattern)
                    substrings = pattern*total
                    
                    if substrings == string and total !=1:
                        print(pattern,total,substrings,"found")
                        return pattern
                    
            print("out")
            return ''
        
        if repeatingPattern(s)!='':
            return True
        return False
        
        