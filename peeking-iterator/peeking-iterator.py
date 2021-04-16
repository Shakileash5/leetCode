# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class node:
    def __init__(self,val):
        self.val = val
        self.next = None

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        listData = iterator.v
        self.root = node(listData[0])
        #print(self.root)
        self.stack = listData
        self.pointer = 0
        self.size = len(listData)
        temp = self.root
        for i in listData[1:]:
            temp.next = node(i)
            temp = temp.next
        #print(self.root.next.next.next.val)
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        #if self.root.next:
        #    print(self.root.val,"peek")
        #    return self.root.val
        if self.pointer<self.size:
            return self.stack[self.pointer]
        
        return None     

    def next(self):
        """
        :rtype: int
        """
        #val = self.root.val
        #print(val,"n")
        #self.root = self.root.next
        val = self.stack[self.pointer]
        #print(val,self.pointer,"next")
        self.pointer+=1
        return val
    def hasNext(self):
        """
        :rtype: bool
        """
        #print(self.root,"g")
        #if self.root==None or self.root.next == None:
        #    return False
        #print(self.pointer,self.pointer == self.size-1)
        if  self.pointer>=self.size:
            return False
        
        return True
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].