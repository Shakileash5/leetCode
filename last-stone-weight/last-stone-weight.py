import heapq

class Heap:
    def __init__(self):
        self.arr = []
        self.size = 0
    
    def heapify(self,idx):
        leftChild = idx*2 + 1
        rightChild = idx*2 + 2
        
        largest = idx
        
        if leftChild<self.size and self.arr[largest]<self.arr[leftChild]:
            largest = leftChild
        if rightChild<self.size and self.arr[largest]<self.arr[rightChild]:
            largest = rightChild
        
        if largest != idx:
            self.arr[largest],self.arr[idx] = self.arr[idx],self.arr[largest]
            self.heapify(largest)
        
        return
    
    def heapifyBottomUp(self,idx):
        parent = (idx-1)//2
        
        if parent>=0:
            if self.arr[idx]>self.arr[parent]:
                self.arr[idx],self.arr[parent] = self.arr[parent],self.arr[idx]
                self.heapifyBottomUp(parent)
        return
    
    def heapPush(self,val):
        self.arr.append(val)
        self.size += 1
        self.heapifyBottomUp(self.size-1)
        return
    
    def heapPop(self):
        if self.size <= 1:
            self.size -= 1
            return self.arr.pop()
        val = self.arr[0]
        self.size -= 1
        self.arr[0] = self.arr.pop()
        self.heapify(0)
        return val
        

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #heapq.heapify(stones)
        if len(stones)<=1:
            return stones[0]
        heapObj = Heap()
        arr = []
        for i in range(len(stones)):
            heapq.heappush(arr,-1*stones[i])
            heapObj.heapPush(stones[i])
        
        #print(heapObj.arr)
            
        while(True):
            print(heapObj.arr)
            if len(heapObj.arr)>=2:
                heavyStone = heapObj.heapPop()#-1*heapq.heappop(arr)
                secondHeavyStone = heapObj.heapPop()#-1*heapq.heappop(arr)
                print(heavyStone,secondHeavyStone)
                if heavyStone != secondHeavyStone:
                    heavyStone = heavyStone - secondHeavyStone
                    heapObj.heapPush(heavyStone)#heapq.heappush(arr,-1*heavyStone)
                    
                print("inside after",heapObj.arr)
            if len(heapObj.arr) == 1:
                return heapObj.arr[0]
            if len(heapObj.arr) == 0:
                break
        return 0
            