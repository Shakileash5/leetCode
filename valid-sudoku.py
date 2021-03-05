# https://leetcode.com/problems/valid-sudoku/
# Problem Description

# Solution

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowList = []
        columnList = []
        boxList = []
        sizeRow = len(board)
        sizeCol = len(board[0])
        for i in range(sizeRow):
            rowList.append(set())
            columnList.append(set())
            boxList.append(set())
        
        for i in range(sizeRow):
            for j in range(sizeCol):
                if board[i][j] != ".":
                    if board[i][j] in rowList[i]:
                        return False
                    if board[i][j] in columnList[j]:
                        return False
                    
                    row = i//3
                    column = j//3
                    
                    if row == 1:
                        column = column+3
                    if row == 2:
                        column = column+6
                        
                    #index = (row%3)*3 + j%3
                    #print(index," Index")
                    if board[i][j] in boxList[column]:
                        return False
                    
                    rowList[i].add(board[i][j])
                    columnList[j].add(board[i][j])
                    boxList[column].add(board[i][j])
        
        return True
                    
                
                
                
        
        
        