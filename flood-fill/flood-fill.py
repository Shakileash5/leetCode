class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        sizeRow = len(image)
        sizeCol = len(image[0])
        visited = set()
        
        def isValid(x,y):
            if x<0 or y<0 or x>=sizeRow or y>=sizeCol:
                return False
            return True
        
        def dfs(i,j,visited,currColor,newColor):
            
            visited.add((i,j))
            image[i][j] = newColor
            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if isValid(x,y) and image[x][y] == currColor and (x,y) not in visited:
                    dfs(x,y,visited,currColor,newColor)
        
        currColor = image[sr][sc]
        
        dfs(sr,sc,visited,currColor,newColor)
        
        return image