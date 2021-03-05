# https://leetcode.com/problems/container-with-most-water/
# Problem Description

# Solution

class Solution:
    def intToRoman(self, num: int) -> str:
        
        romans = [
            {
                "1" : "I",
                "5" : "V",
            },
            {
                "1" : "X",
                "5" : "L",  
            },
            {
                "1" : "C",
                "5" : "D",  
            },
            {
                "1" : "M", 
            }
        ]
        
        res = ""
        number = num
        count = 0
        while num>0:
            print(count,res)
            n = int(num%10)
            if n<4:
                res = int(n)* romans[count]["1"] + res   
            elif n==4:
                res = romans[count]["1"]+romans[count]["5"] + res
            elif n==5:
                res = romans[count]["5"] + res
            elif n<9:
                res = romans[count]["5"]+ int(n-5)* romans[count]["1"] + res
            elif n==9:
                res = romans[count]["1"] + romans[count+1]["1"] + res
            num=int(num/10)  
            print(num)
            count+=1
        return res