class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        queue = [[0,False,0]]
        seen = set((0,False))
        
        def isValid(pos,back):
            if 0<=pos<= 6000 and (pos,back) not in seen and pos not in forbidden:
                return True
            return False
        
        
        while queue:
            for _ in range(len(queue)):
                pos,back,step = queue.pop(0)
                if pos == x:
                    return step
                if isValid(pos+a,False):
                    seen.add((pos+a,False))
                    queue.append([pos+a,False,step+1])
                if not back and isValid(pos-b,True):
                    seen.add((pos-b,True))
                    queue.append([pos-b,True,step+1])
        return -1
                    
                
                