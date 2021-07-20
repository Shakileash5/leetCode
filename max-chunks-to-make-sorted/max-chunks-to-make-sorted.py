import bisect
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        size = len(arr)
        
        noOfChunks = 0
        
        stack = []
        
        #for i in range(size-1,-1,-1):
        #    while stack and stack[-1]<arr[i]:
        #        stack.pop()
        #    stack.append(arr[i])
        #print(stack)
        i = 0
        """while(i<size):
            if arr[i] != i:
                idx = arr.index(i)
                #print(idx,arr[i],i)
                while(i<idx):
                    if arr[i]>(idx):
                        idx = arr.index(i)
                    i += 1
            noOfChunks += 1
                    
            i += 1"""
        
        while(i<size):
            if i==0:
                if arr[i] != 0:
                    stack.append(arr[i])
                else:
                    noOfChunks += 1
            elif stack:
                #print(stack,i)
                if stack[-1] == i:
                    if arr[i]<stack[-1]:
                        noOfChunks+=1
                        stack.pop()
                    else:
                        stack[-1] = arr[i]
                elif stack[-1]<arr[i]:
                    stack[-1] = arr[i]
            elif arr[i]==i:
                noOfChunks += 1
            else:
                stack.append(arr[i])
            i+=1
        
        return noOfChunks
                
        