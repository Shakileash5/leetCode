class Solution:
    def solveTwo(self,board):
        visited = set()
        sizeR = len(board)
        sizeC = len(board[0])
        markArr = set()
        flag = [False]
        res = []
        
        def isBorder(i,j):
            if i == 0 or j == 0 or i == sizeR-1 or j == sizeC-1:
                return True
            return False
        
        def moveCoords(i,j):
            visited.add((i,j))
            markSet.add((i,j))
            if isBorder(i,j):
                flag[0] = True
            if 0<=(i+1)<sizeR and 0<=j<sizeC:
                if (i+1,j) not in visited and board[i+1][j] == 'O':
                    moveCoords(i+1,j)
            if 0<=(i-1)<sizeR and 0<=j<sizeC:
                if (i-1,j) not in visited and board[i-1][j] == 'O':
                    moveCoords(i-1,j)
            if 0<=(i)<sizeR and 0<=(j+1)<sizeC:
                if (i,j+1) not in visited and board[i][j+1] == 'O':
                    moveCoords(i,j+1)
            if 0<=(i)<sizeR and 0<=(j-1)<sizeC:
                if (i,j-1) not in visited and board[i][j-1] == 'O':
                    moveCoords(i,j-1)
            return
        
        for i in range(sizeR):
            for j in range(sizeC):
                if (i,j) not in visited and board[i][j] == "O":
                    markSet = set()
                    flag = [False]
                    moveCoords(i,j)
                    if flag[0] == False:
                        for val in markSet:
                            markArr.add(val)
                    #print(visited,markSet,flag)
        #print("fe",markArr)
        for (i,j) in markArr:
            board[i][j] = 'X'
        return []
        
        
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        visitedSet = set()
        connectedList = []
        borderFlag = [0]
        
        def isBorder(i,j,m,n):
            if i == 0 or j == 0:
                return True
            if i == m-1 or j == n-1:
                return True
            
            return False
        
        def addVisited(connectedList):
            for i in connectedList:
                visitedSet.add(i)
            return
        
        def exploreConnections(i,j,m,n,to_ignore):
            if i>=m or j>=n:
                return
            if i<0 or j<0:
                return
            if board[i][j] == 'X':
                return
            
            res = isBorder(i,j,m,n)
            if res:
                borderFlag[0] = 1 
            connectedList.append((i,j))
            if (i,j) not in to_ignore:
                to_ignore.add((i,j))
                exploreConnections(i+1,j,m,n,to_ignore)
                exploreConnections(i,j-1,m,n,to_ignore)
                exploreConnections(i,j+1,m,n,to_ignore)
                exploreConnections(i-1,j,m,n,to_ignore)
            #exploreConnections(i,j-1,m,n)
            
            return
        
        def convertToX(connectedList):
            for i in range(len(connectedList)):
                board[connectedList[i][0]][connectedList[i][1]] = "X"
            
            return
        
        """m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                borderFlag[0] = 0
                connectedList = []
                
                if board[i][j] == "O":
                    if (i,j) not in visitedSet:
                        exploreConnections(i,j,m,n,set())
                        if borderFlag[0] == 1:
                            addVisited(connectedList)
                        else:
                            convertToX(connectedList)"""
        self.solveTwo(board)
        return              
                    
                    
            