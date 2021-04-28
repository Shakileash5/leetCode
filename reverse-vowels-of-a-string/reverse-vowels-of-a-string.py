class Solution:
    def reverseVowels(self, s: str) -> str:
        size = len(s)
        start = 0
        end = size-1
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        
        while(start<end):
            while(start<size and (s[start] not in vowels)):
                start+=1
            
            while(end>=0 and (s[end] not in vowels)):
                end-=1
            
            if start<end:
                #print(start,end)
                temp = s[start]
                s = s[:start] + s[end] + s[start+1:]
                s = s[:end] + temp + s[end+1:]
                start+=1
                end-=1
                #print("em",start,end)
            else:
                break
        
        return s