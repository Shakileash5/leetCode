class Solution:
    def canWinNim(self, n: int) -> bool:
        
        def backtrack(turn,stoneLevel):
            if stoneLevel>n:
                print("cameHere")
                return False
            if stoneLevel == n:
                print(turn,stoneLevel,"gotIt")
                if turn == 0:
                    return True
                else:
                    print("returned")
                    return False
            print(turn,stoneLevel)
            if turn == 1:
                if backtrack(0,stoneLevel+1):
                    return True
                print()
                if backtrack(0,stoneLevel+2):
                    return True
                if backtrack(0,stoneLevel+3):
                    return True
            else:
                if backtrack(1,stoneLevel+1):
                    print("otHere")
                    return True
                if backtrack(1,stoneLevel+2):
                    return True
                if backtrack(1,stoneLevel+3):
                    return True
            
            return False
        
        #backtrack(1,0)
        #backtrack is not elegible
        
        return n%4