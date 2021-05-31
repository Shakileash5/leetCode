class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        
        if len(self.stack)==0:
            self.minStack.append(val)
        else:
            if self.minStack[-1]>val:
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])
        self.stack.append(val)
        return   

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()