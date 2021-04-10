from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.graphNodes = defaultdict(list)
        self.vertices = vertices
    
    def addEdge(self,source,destination):
        self.graphNodes[source].append(destination)
    
    def recur(self,node,visited,stack):
         
        visited.add(node)
        
        for neighbours in self.graphNodes[node]:
                if neighbours not in visited:
                    self.recur(neighbours,visited,stack)
        
        stack.append(node)
            
    
    def topologicalSort(self):
        visited = set()
        stack = []
        for i in range(self.vertices):
            if i not in visited:
                self.recur(i,visited,stack)
        
        print(stack,"here")
        return stack
    
    def cylicDetectionUtil(self,node,visited,recursionStack):
        if node not in self.graphNodes:
            return True
        if node in visited:
            return True
        if node in recursionStack:
            return False
        
        recursionStack.add(node)
        for i in self.graphNodes[node]:
            if self.cylicDetectionUtil(i,visited,recursionStack) == False:
                return False
        visited.add(node)
    
    def cylicDetection(self):
        visited = set()
        for i in range(self.vertices):
            recursionStack = set()
            if i not in visited:
                if self.cylicDetectionUtil(i,visited,recursionStack) == False:
                    return False
        return True
        
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = Graph(numCourses)
        
        for i in prerequisites:
            graph.addEdge(i[0],i[1])
        
        print(graph.graphNodes)
        if graph.cylicDetection() == False:
            return []
        
        res = graph.topologicalSort()
        
        return res