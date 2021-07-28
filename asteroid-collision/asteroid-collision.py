class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        size = len(asteroids)
        stack = []
        
        for i in range(size):
            stack.append(asteroids[i])
            if len(stack)>=2:
                while len(stack)>=2 and stack[-1]<0 and stack[-2]>0:
                    asteroid1 = stack.pop()
                    asteroid2 = stack.pop()
                    if abs(asteroid1)>asteroid2:
                        stack.append(asteroid1)
                    elif abs(asteroid1)<asteroid2:
                        stack.append(asteroid2)
        #print(stack)
        return stack