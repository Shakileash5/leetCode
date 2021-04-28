class Heap:
    def __init__(self,arr,size):
        self.size = size
        self.arr = arr
    
    def leftChild(self,pos):
        return pos*2+1
    
    def rightChild(self,pos):
        return pos*2+2
    
    def parent(self,pos):
        return (pos-1)//2
    
    def swap(self,left,right):
        #print(self.arr[left],self.arr[right])
        self.arr[left],self.arr[right] = self.arr[right],self.arr[left]
        return
    
    def heapify(self,idx,size):      
        left = self.leftChild(idx)
        right = self.rightChild(idx)
        largest = idx
        
        if left<self.size and self.arr[left][0] > self.arr[largest][0]:
            largest = left
        if right<self.size and self.arr[right][0] > self.arr[largest][0]:
            largest = right
        
        if largest!= idx:
            self.swap(largest,idx)
            self.heapify(largest,self.size)
        
        return
    
    def buildHeap(self):
        start = self.size//2 - 1
        for i in range(start,-1,-1):
            self.heapify(i,self.size)

    def extractMax(self):
        if self.arr!=[]:
            val = self.arr[0]
            self.arr[0] = self.arr[self.size-1]
            self.size = self.size-1
            self.heapify(0,self.size)
            return val
        return None
    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = {}
        for val in nums:
            keys = hashMap.keys()
            if val not in keys:
                hashMap[val] = [1,val]
            else:
                hashMap[val][0] += 1
        arr = []
        for key in hashMap.keys():
            arr.append(hashMap[key])
        
        #print(arr,hashMap)
        heapObj = Heap(arr,len(arr))
        heapObj.buildHeap()
        #print(heapObj.arr)
        res = []
        for i in range(k):
            res.append(heapObj.extractMax()[1])
        
        return res
        #print(heapObj.extractMax(),heapObj.extractMax())
        
        
        
        