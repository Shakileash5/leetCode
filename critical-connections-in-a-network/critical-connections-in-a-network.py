from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        bridge = []
        self.time = 0
        self.disc = [-1]*n
        self.low = [-1]*n
        
        for src,dest in connections:
            graph[src].append(dest)
            graph[dest].append(src)
        
        def dfs(node,parent):
            if self.disc[node]!=-1:
                return
            
            self.disc[node] = self.time
            self.low[node] = self.time
            self.time += 1
            
            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                
                dfs(neighbour,node)
                
                self.low[node] = min(self.low[node],self.low[neighbour])
                if self.disc[node]<self.low[neighbour]:
                    bridge.append([node,neighbour])
            return
        
        dfs(0,-1)
        return bridge
            
            
            
            