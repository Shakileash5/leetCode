class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        sizeRow = len(board)
        sizeCol = len(board[0])
        size = len(word)
        visited = set()
        
        def backtrack(idx,idxR,idxC):
            if idx>=size:
                return True
            visited.add((idxR,idxC))
            #print(idxR,idxC,idx)
            for i,j in [(0,1),(1,0),(-1,0),(0,-1)]:
                x = i+idxR
                y = j+idxC
                if 0<=x<sizeRow and 0<=y<sizeCol and (x,y) not in visited:
                    #print(x,y)
                    if word[idx] == board[x][y]:
                        if backtrack(idx+1,x,y):
                            return True
            visited.remove((idxR,idxC))
            return False
        
        for i in range(sizeRow):
            for j in range(sizeCol):
                if board[i][j] == word[0]:
                    visited = set()
                    if backtrack(1,i,j):
                        return True
        return False
        