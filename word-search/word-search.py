class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        sizeRow = len(board)
        sizeCol = len(board[0])
        size = len(word)
        
        def searchWord(idxR,idxC,idx,visited):
            if idx>=size:
                return True
            
            visited.add((idxR,idxC))
            for x,y in [(idxR+1,idxC),(idxR,idxC+1),(idxR-1,idxC),(idxR,idxC-1)]:
                if 0<=x<sizeRow and 0<=y<sizeCol:
                    if board[x][y] == word[idx] and (x,y) not in visited:
                        if searchWord(x,y,idx+1,visited):
                            return True
            visited.remove((idxR,idxC))
            return False
        
        #print(searchWord(0,0,1,set()))
        for i in range(sizeRow):
            for j in range(sizeCol):
                if board[i][j] == word[0]:
                    visited = set()
                    if searchWord(i,j,1,visited):
                        return True
        
        return False