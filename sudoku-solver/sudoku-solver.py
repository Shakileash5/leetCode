class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        sizeRow = len(board)
        sizeCol = len(board[0])
        rowSet = [[] for i in range(sizeRow)]
        colSet = [[] for j in range(sizeCol)]
        missingBoxes = [[[] for i in range(3)] for j in range(3)]
        #print(missingBoxes)
        holes = 0
        def getSquareIdx(x,y):
            rowMajor = x*9 + y
            yidx = math.floor((y % 9) / 3)
            xidx = math.floor(rowMajor / (9 * 3))
            return xidx,yidx
        
        for i in range(sizeRow):
            for j in range(sizeCol):
                if board[i][j]!='.':
                    rowSet[i].append(int(board[i][j]))
                    colSet[j].append(int(board[i][j]))
                    x,y = getSquareIdx(i,j)
                    missingBoxes[x][y].append(int(board[i][j]))
                else:
                    holes += 1
        def recur(idxR,idxC,filled):
            if idxR == 9:
                #print(board,"gfieuw")
                return True
            next_r, next_c = (idxR, idxC + 1) if idxC != 8 else (idxR + 1, 0)
            if board[idxR][idxC] != '.':
                #print(next_r,next_c)
                return recur(next_r,next_c,filled)
            #print("so",idxR,idxC)
            #for i in range(idxR,sizeRow):
            #for j in range(idxC,sizeCol):
            #if board[i][j] == '.':
            x,y = getSquareIdx(idxR,idxC)
            i = idxR
            j = idxC
            for num in range(1,10):
                #print(num,board[i][j])
                if num not in missingBoxes[x][y]:
                    if num not in rowSet[i] and num not in colSet[j]:
                        board[i][j] = str(num)
                        missingBoxes[x][y].append(num)
                        rowSet[i].append(num)
                        colSet[j].append(num)
                        #print("here",board)
                        if recur(next_r,next_c,filled+1):
                            return True
                        missingBoxes[x][y].pop()
                        rowSet[i].pop()
                        colSet[j].pop()
                        board[i][j] = '.'
            return
        
        #print(missingBoxes,0)
        recur(0,0,0)
        #print(board)
        return