# https://leetcode.com/problems/roman-to-integer/
# Problem Description

# Solution

class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            
                "I" : "1",
                "V" : "5",
                "X" : "10",
                "L" : "50",  
                "C" : "100",
                "D" : "500",  
                "M" : "1000", 
            }
        res = ""
        size = len(s)
        i = 0
        num = 0
        while i<size :
            
            if s[i] == "I":
                num +=1
            if s[i] == "V":
                if i!=0 and s[i-1] == "I":
                    num -=1
                    num+=4
                else:
                    num+=5
            if s[i] == "X":
                if i!=0 and s[i-1] == "I":
                    num-=1
                    num+=9
                else:
                    num+=10
            if s[i] == "L":
                 if i!=0 and s[i-1] == "X":
                    num-=10
                    num+=40
                 else:
                    num+=50
            if s[i] == "C":
                if i!=0 and s[i-1] == "X":
                    num-=10
                    num+=90
                else:
                    num+=100
            if s[i] == "D":
                if i!=0 and s[i-1] == "C":
                    num-=100
                    num+=400
                else:
                    num+=500 
            if s[i] == "M":
                if i!=0 and s[i-1] == "C":
                    num-=100
                    num+=900
                else:
                    num+=1000
            i=i+1
        return num   