class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        answer = [0] * n
        graph = {}
        types = [1,2,3,4]
        if len(paths) == 0:
            return [1]*n
        
        for i in range(len(paths)):
            if paths[i][0] in graph:
                graph[paths[i][0]].append(paths[i][1])
            else:
                graph[paths[i][0]] = [paths[i][1]]
            if paths[i][1] in graph:
                graph[paths[i][1]].append(paths[i][0])
            else:
                graph[paths[i][1]] = [paths[i][0]]
        
        
        def bfs():
            
            for i in range(n):
                if answer[i]!=0:
                    continue
                temp = set([1,2,3,4])
                if i+1 in graph:
                    for neighbour in graph[i+1]:
                        if answer[neighbour-1] in temp:
                            temp.remove(answer[neighbour-1])
                answer[i] = temp.pop()
        bfs()
        return answer
                    
                            