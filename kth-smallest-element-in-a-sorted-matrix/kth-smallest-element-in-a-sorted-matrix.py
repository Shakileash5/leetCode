import heapq
import bisect
class Heap:
    def __init__(self,size=0):
        self.size = size
        self.arr = []
    
    def swap(self,left,right):
        self.arr[left],self.arr[right] = self.arr[right],self.arr[left]
        return
    
    def heapify(self,pos):
        left = pos*2 + 1
        right = pos*2 + 2
        largest = pos
        
        if left<self.size and self.arr[left]<self.arr[largest]:
            largest = left
        if right<self.size and self.arr[right]<self.arr[largest]:
            largest = right
        
        if largest!=pos:
            self.swap(largest,pos)
            self.heapify(largest)
        return
    
    def buildHeap(self,arr):
        lastLeaf = self.size//2 - 1
        self.arr = arr
        for i in range(lastLeaf,-1,-1):
            self.heapify(i)
        return
    
    def insert(self,val):
        self.size+=1
        self.arr.append(val)
        cur = self.size-1
        parent = (self.size-1)//2
        #print(self.arr,cur,parent)
        while self.arr[cur]<self.arr[parent]:
            self.swap(parent,cur)
            cur = parent
            parent = (cur+1)//2
        return
    
    def extractMax(self):
        val = self.arr[0]
        self.arr[0] = self.arr[self.size-1]
        self.size -=1
        self.heapify(0)
        return val
    
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        arr = []
        res = [-1]
        heapq.heapify(arr)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(arr,-1*matrix[i][j])
        
        #heapObj.heapify(0)
        #print(heapObj.arr) 
        for i in range(k):
            val = heapq.heappop(arr)  
        #heapObj = Heap(arr,len(arr))
        #heapObj.buildHeap(arr)
        def searchIndex(val):
            low = -2**31
            count = 0
             
            for row in matrix:
                idx = bisect.bisect(row,val)
                count+=idx
                if idx>0:
                    low = max(row[idx-1],low)
            return count,low
            
            
        def binarySearch(left,right):
            #print(left,right)
            if left>right:
                return
            
            mid = (left+right)//2
            count,val = searchIndex(mid)
            #print(count,val)
            if count>=k:
                res[0] = val
                #print(val)
                binarySearch(left,mid-1)
            else:
                binarySearch(mid+1,right)
                
        binarySearch(matrix[0][0],matrix[-1][-1])
        #print(res)
        return res[0]