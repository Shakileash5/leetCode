class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        
        for i in range(size//2):
            for j in range(i,size-i-1):
                matrix[i][j],matrix[j][size-1-i] = matrix[j][size-1-i],matrix[i][j]
                matrix[i][j],matrix[size-1-i][size-1-j] = matrix[size-1-i][size-1-j],matrix[i][j]
                matrix[i][j],matrix[size-1-j][i] = matrix[size-1-j][i],matrix[i][j]
        return