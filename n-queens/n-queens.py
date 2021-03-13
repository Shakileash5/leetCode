class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def isSafe(board,row,col):
            for i in range(col): 
                if board[row][i] == 1: 
                    return False

            # Check upper diagonal on left side 
            for i, j in zip(range(row, -1, -1),  
                            range(col, -1, -1)): 
                if board[i][j] == 1: 
                    return False

            # Check lower diagonal on left side 
            for i, j in zip(range(row, n, 1),  
                            range(col, -1, -1)): 
                if board[i][j] == 1: 
                    return False

            return True
        
        def backtrack(board,col):
            
            if col>=n:
                #print(board)
                temp = []
                for i in range(n):
                    txt = ''
                    for j in range(n):
                        if board[i][j] == 0:
                            txt+="."
                        else:
                            txt+="Q"
                    temp.append(txt)
                res.append(temp)
                #print(res)
                            
                            
                return True
            else:
                for i in range(n):
                    if isSafe(board,i,col):
                        board[i][col] = 1
                        backtrack(board,col+1)
                        board[i][col] = 0
            return False
        res = []
        board = [[0 for j in range(n)] for i in range(n)]
        #print(board)
        resQ = backtrack(board,0)
        return res
        
        