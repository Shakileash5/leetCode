class Graph:
    def __init__(self,vertices):
        self.graphNode = {}
        self.vertices = vertices
        
    def addEdge(self,source,destination):
        if source not in self.graphNode:
            self.graphNode[source] = [destination]
        else:
            self.graphNode[source].append(destination)
        return
    
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [_ for _ in range(numCourses)]
        
        def dfs(node):
            
            if node not in graph.graphNode:
                return True
            
            if node in visitedSet:
                return True
            
            if node in recursionSet:
                return False
            
            recursionSet.add(node)
            #print("added",node)
            #if node in graph.graphNode.keys():
            for nodes in graph.graphNode[node]:
                if dfs(nodes) == False:
                    return False
            #else:
            #    return True
            visitedSet.add(node)
            #print("no",node)
            return True
        
        graph = Graph(numCourses)
        for i in prerequisites:
            graph.addEdge(i[0],i[1])
        
        print(graph.graphNode)
        visitedSet = set()
        
        for i in courses:
            recursionSet = set()
            if dfs(i) == False:
                return False
                
        return True
            