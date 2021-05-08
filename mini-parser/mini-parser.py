# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        
        stack = []
        size = len(s)
        num = ""
        flag = 0
        sflag = 0
        neg = 0
        for i in range(size):
            if s[i] == "[":
                flag = 1
                node = NestedInteger()
                stack.append(node)
            elif s[i] == "]":
                if sflag == 1:
                    if num !="" :
                        stack[-1].add(NestedInteger(int(num)))
                        num = ""
                    sflag = 0
                        
                val = stack.pop()
                if stack:
                    stack[-1].add(val)
                else:
                    break
            elif s[i].isnumeric():
                num+=s[i]
                sflag = 1
            elif s[i] =="-":
                num+=s[i]
            elif s[i] == ",":
                if num!='':
                    stack[-1].add(NestedInteger(int(num)))
                
                num = ""
                sflag = 0
        
        if flag == 0:
            return NestedInteger(int(s))
        return val
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        