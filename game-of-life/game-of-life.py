class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        sizeRow = len(board)
        sizeCol = len(board[0])
        
        def totalNeighbours(i,j):
            count = 0
            print(i,j)
            if i>0 and j<sizeCol and board[i-1][j] == 1:
                count+=1
            if j>0 and i<sizeRow and board[i][j-1] == 1:
                count+=1
            if i>0 and j>0 and board[i-1][j-1] == 1:
                count+=1
            if i>0 and (j+1)<sizeCol and board[i-1][j+1] == 1:
                count+=1
            if (j+1)<sizeCol and i<sizeRow and board[i][j+1] == 1:
                count+=1
            if (i+1)<sizeRow and (j+1)<sizeCol and board[i+1][j+1] == 1:
                count+=1
            if (i+1)<sizeRow and j<sizeCol and board[i+1][j] == 1:
                count+=1
            if (i+1)<sizeRow and j>0 and board[i+1][j-1] == 1:
                count+=1
            
            return count
        
        
        #print(totalNeighbours(2,1))
        idx = 0
        #addZeros = set()
        lifeTaker = set()
        while(idx<1):
            for i in range(sizeRow):
                for j in range(sizeCol):
                    print("idx",i,j)
                    neighbours = totalNeighbours(i,j)
                    if neighbours < 2 and board[i][j]!=0:
                        #board[i][j] = 1
                        lifeTaker.add((i,j,0))
                    elif neighbours >3 and board[i][j] == 1:
                        #board[i][j] = 0
                        lifeTaker.add((i,j,0))
                    elif neighbours == 3 and board[i][j] == 0:
                        #board[i][j] = 1
                        lifeTaker.add((i,j,1))
            for i,j,val in lifeTaker:
                board[i][j] = val
            #print(board)
            i,j=0,0
            idx+=1
        