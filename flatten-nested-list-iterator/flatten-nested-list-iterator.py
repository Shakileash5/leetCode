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
    def recur(self,node):
        for element in node:
            if element.isInteger():
                self.stack.append(element.getInteger())
            else:
                self.recur(element.getList())
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self.recur(nestedList)
    
    def next(self) -> int:
        #print("fw",self.stack[-1][self.idxStack[-1]].getList())
        val = self.stack.pop(0)
        return val
    
    def hasNext(self) -> bool:
        if len(self.stack) == 0:
                return False
        return True

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())