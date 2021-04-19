class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        sizeSecret = len(secret)
        sizeGuess = len(guess)
        cows = 0
        bulls = 0
        
        for i in range(sizeSecret):
            if secret[i] == guess[i]:
                bulls+=1
                secret = secret[:i]+"#"+secret[i+1:]
                guess = guess[:i]+"#"+guess[i+1:]
                
        for i in range(sizeSecret):
            if secret[i] != "#":
                flag = 0
                for j in range(sizeGuess):
                    if flag==0 and guess[j] != "#":
                        if guess[j] == secret[i]:
                            cows+=1

                            guess = guess[:j]+"#"+guess[j+1:]
                            flag = 1
                            
        
        #print(bulls,cows)
        return str(bulls)+"A"+str(cows)+"B"