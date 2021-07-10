class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        graph = {}
        visited = set()
        routesToChange = [0]
        
        for i in range(n-1):
            if connections[i][0] not in graph:
                graph[connections[i][0]] = [[connections[i][1],1]]
            else:
                graph[connections[i][0]].append([connections[i][1],1])
            
            if connections[i][1] not in graph:
                graph[connections[i][1]] = [[connections[i][0],0]]
            else:
                graph[connections[i][1]].append([connections[i][0],0])
        
        #print(graph)
        
        def dfsUtil(node):
            visited.add(node)
            #print(node)
            for neighbors in graph[node]:
                if neighbors[0] not in visited:
                    if neighbors[1] == 1:
                        routesToChange[0] += 1
                        #print('fake',node,neighbors)
                    dfsUtil(neighbors[0])
            return
        
        dfsUtil(0)
        
        return routesToChange[0]