class Heap:
    def __init__(self,size=0):
        self.size = size
        self.arr = [None]*size
    
    def swap(self,left,right):
        self.arr[left],self.arr[right] = self.arr[right],self.arr[left]
        return
    
    def heapify(self,pos):
        leftChild = pos*2+1
        rightChild = pos*2+2
        largest = pos
        
        if leftChild<self.size and self.arr[leftChild][0]>self.arr[largest][0]:
            largest = leftChild
        if rightChild<self.size and self.arr[rightChild][0]>self.arr[largest][0]:
            largest = rightChild
        
        if largest!=pos:
            self.swap(largest,pos)
            self.heapify(largest)
        
        return
    
    def buildHeap(self,arr):
        self.arr = arr
        self.size = len(arr)
        till = self.size//2-1
        for i in range(till,-1,-1):
            self.heapify(i)
        return
    
    def extractMax(self):
        top = self.arr[0]
        self.arr[0] = self.arr[self.size-1]
        self.size -= 1
        self.heapify(0)
        return top
        
import heapq        
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        arr = []
        hashMap = {}
        arr2 =[]
        for i in words:
            if i not in hashMap.keys():
                hashMap[i] = 1
            else:
                hashMap[i] += 1
        for key in hashMap.keys():
            #arr.append([hashMap[key],key])
            heapq.heappush(arr2,[-1*hashMap[key],key])
        #heapObj = Heap()
        #heapObj.buildHeap(arr)
        #print(heapObj.arr)
        #print(arr2)
        res = []
        for i in range(k):
            #res.append(heapObj.extractMax()[1])
            res.append(heapq.heappop(arr2)[1])
        return res
        
        
        
        
        
        