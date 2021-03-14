class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        sizeR = len(board)
        sizeC = len(board[0])
        
        sizeW = len(word)
        
        def backtrack(i,j,idx,res,visited):
            
            if res == word:
                #print(res)
                return True
            if len(res) == len(word) and res!=word:
                return False
            #print(visited,"visis")
            if j+1<sizeC and (i,j+1) not in visited and board[i][j+1] == word[idx]:
                visited.add((i,j+1))
                if backtrack(i,j+1,idx+1,res+word[idx],visited):
                    return True
                visited.remove((i,j+1))
            if j-1>=0 and (i,j-1) not in visited and board[i][j-1] == word[idx]:
                visited.add((i,j-1))
                if backtrack(i,j-1,idx+1,res+word[idx],visited):
                    return True
                visited.remove((i,j-1))
            if i+1<sizeR and (i+1,j) not in visited and board[i+1][j] == word[idx]:
                visited.add((i+1,j))
                if backtrack(i+1,j,idx+1,res+word[idx],visited):
                    return True
                visited.remove((i+1,j))
            if i-1>=0 and (i-1,j) not in visited and board[i-1][j] == word[idx]:
                visited.add((i-1,j))
                if backtrack(i-1,j,idx+1,res+word[idx],visited):
                    return True
                visited.remove((i-1,j))
            
            return False
        visited = set()
        
        for i in range(sizeR):
            for j in range(sizeC):
                
                if board[i][j] == word[0]:
                    #print(i,j)
                    visited.add((i,j))
                    res = backtrack(i,j,1,word[0],visited)
                    visited.remove((i,j))
                    #print("aftee",res)
                    if res == True:
                        return True
        
        #print(backtrack(0,0,1,"A",visited))
        return False