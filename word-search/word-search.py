class Solution:
    
    def dfs(self,board,idxR,idxC,word,visited,sizeR,sizeC,idx):
        if (idxR,idxC) in visited:
            return False
        if idx>=len(word):
            return True
        visited.add((idxR,idxC))
        #print(idxR,idxC)
        for x,y in [(0,1),(1,0),(0,-1),(-1,0)]:
            if 0<= (x+idxR) and (x+idxR)<sizeR and 0<=(y+idxC) and (y+idxC)<sizeC:
                if board[(x+idxR)][(y+idxC)] == word[idx]:
                    if self.dfs(board,x+idxR,y+idxC,word,visited,sizeR,sizeC,idx+1):
                        return True
        visited.remove((idxR,idxC))
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        sizeR = len(board)
        sizeC = len(board[0])
        size = len(word)
        
        for i in range(sizeR):
            for j in range(sizeC):
                if board[i][j] == word[0]:
                    res = self.dfs(board,i,j,word,set(),sizeR,sizeC,1)
                    if res:
                        return True
        
        return False