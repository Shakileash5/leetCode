class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack == []:
            self.minStack.append(val)
        else:
            top = self.minStack[-1]
            if top>=val:
                self.minStack.append(val)
            elif top<val:
                #val = self.minStack.pop()
                self.minStack.append(self.minStack[-1])
                #self.minStack.append(val)
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