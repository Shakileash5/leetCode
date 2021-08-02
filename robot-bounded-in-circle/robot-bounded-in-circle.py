class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        size = len(instructions)
        cur = [0,0]
        currDir = 0
        
        def move(dir_,curr):
            if dir_ == 0:
                curr = [curr[0],curr[1]+1]
            if dir_ == 1:
                curr = [curr[0]+1,curr[1]]
            if dir_ == 2:
                curr = [curr[0],curr[1]-1]
            if dir_ == 3:
                curr = [curr[0]-1,curr[1]]
            
            return curr
        
        for i in range(size):
            if instructions[i] == 'G':
                cur = move(currDir,cur)
            elif instructions[i] == 'L':
                if currDir == 0:
                    currDir = 1
                elif currDir == 1:
                    currDir = 2
                elif currDir == 2:
                    currDir = 3
                elif currDir == 3:
                    currDir = 0
            elif instructions[i] == 'R':
                if currDir == 0:
                    currDir = 3
                elif currDir == 3:
                    currDir = 2
                elif currDir == 2:
                    currDir = 1
                elif currDir == 1:
                    currDir = 0
            print(cur,currDir)
        print(cur,currDir)
        #print(cur,radius) 
        #dist = ((cur[0])**2+cur[1]**2)**0.5
        if cur==[0,0] or currDir!=0:
            return True
        return False