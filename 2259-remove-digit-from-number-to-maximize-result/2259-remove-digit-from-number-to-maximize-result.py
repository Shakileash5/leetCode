class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        largerNum = 0
        lastIdx = 0
        for i in range(len(number)):
            #print("af",i,number[i])
            if number[i] == digit:
                #print("same",digit)
                if i != len(number)-1 and int(digit)<int(number[i+1]):
                    #print(number[:i]+number[i+1:])
                    return number[:i]+number[i+1:]
                else:
                    lastIdx = i
                    
        if number[-1] == digit:
            lastIdx = len(number)-1
        return number[:lastIdx]+ number[lastIdx+1:]