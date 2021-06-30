class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        size = len(bank)
        
        queue = []
        queue.append(start)
        mutations = 0
        visited = set()
        
        while queue:
            if end in queue:
                return mutations
            children = []
            while queue:
                gene = queue.pop(0)
                if gene not in visited:
                    visited.add(gene)
                    for b in bank:
                        if len([b[i] for i in range(0, len(b)) if b[i] != gene[i]]) == 1:
                            children.append(b)
                        #children.append(bank[idx])
            mutations += 1
            queue = children[:]
        
        return -1            
                
                    
            
        