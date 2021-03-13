class Solution:
    def totalNQueens(self, n: int) -> int:
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
                res[0]+=1           
                return True
            else:
                for i in range(n):
                    if isSafe(board,i,col):
                        board[i][col] = 1
                        backtrack(board,col+1)
                        board[i][col] = 0
            return False
        res = [0]
        board = [[0 for j in range(n)] for i in range(n)]
        #print(board)
        resQ = backtrack(board,0)
        return res[0]
        