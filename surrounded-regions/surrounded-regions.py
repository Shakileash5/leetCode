class Solution:
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
        
        m = len(board)
        n = len(board[0])
        
        #exploreConnections(1,1,m,n)
        #print(connectedList,borderFlag)
        #convertToX(connectedList)
        #print(board)
        
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
                            convertToX(connectedList)
        #print(board)
        return                    
                    
                    
            