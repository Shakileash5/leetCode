"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        
        visited = set()
        res = []
        
        def binarySearch(x,y):
            visited.add((x,y))
            funcVal = customfunction.f(x,y)
            if funcVal>z:
                return
            if funcVal == z:
                res.append([x,y]) 
            if (x+1,y) not in visited:
                binarySearch(x+1,y)
            if (x,y+1) not in visited:
                binarySearch(x,y+1)
        
        binarySearch(1,1)
        return res