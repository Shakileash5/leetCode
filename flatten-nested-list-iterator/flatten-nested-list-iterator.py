# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nums = []
        self.size = 0
        self.idx = 0
        
        def recur(list_):
            for val in list_:
                if val.isInteger():
                    self.nums.append(val.getInteger())
                else:
                    recur(val.getList())
            return
        recur(nestedList)
        self.size = len(self.nums)
    
    def next(self) -> int:
        val = self.nums[self.idx]
        self.idx += 1
        return val
        
    
    def hasNext(self) -> bool:
        return True if self.idx<self.size else False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())