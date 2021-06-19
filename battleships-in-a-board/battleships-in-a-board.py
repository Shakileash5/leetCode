class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        sizeRow = len(board)
        sizeCol = len(board[0])
        count = 0
        
        def isValid(x,y,visited):
            if x<0 or y<0 or x>=sizeRow or y>=sizeCol:
                return False
            if visited[x][y]:
                return False
            return True
        
        def dfs(idxR,idxC,direction):
            visited[idxR][idxC] = True
            if direction == 1:
                for x,y in [(idxR+1,idxC),(idxR-1,idxC)]:
                    if isValid(x,y,visited) and board[x][y] == 'X':
                        dfs(x,y,direction)
            else:
                for x,y in [(idxR,idxC+1),(idxR,idxC+1)]:
                    if isValid(x,y,visited) and board[x][y] == 'X':
                        dfs(x,y,direction)
            return
        
        visited = [[False for j in range(sizeCol)] for i in range(sizeRow)]
        for i in range(sizeRow):
            for j in range(sizeCol):
                if visited[i][j] == False and board[i][j] == 'X':
                    if j+1<sizeCol and board[i][j+1] == 'X':
                        dfs(i,j,0)
                    else:
                        #print("insid",i,j)
                        dfs(i,j,1)
                    count += 1
                    
        return count
                
            