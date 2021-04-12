class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
        self.currentQueue = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.currentQueue == 0:
            self.queue2.append(x)
            while len(self.queue1)!=0:
                self.queue2.append(self.queue1.pop(0))
            self.currentQueue = 1
        else:
            self.queue1.append(x)
            while len(self.queue2)!=0:
                self.queue1.append(self.queue2.pop(0))
            self.currentQueue = 0
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        popped = None
        if self.currentQueue == 0 and self.queue1: 
            popped = self.queue1.pop(0)
        elif self.queue2:
            popped = self.queue2.pop(0)
        
        return popped

    def top(self) -> int:
        """
        Get the top element.
        """
        top = None
        if self.currentQueue == 0 and self.queue1:
            top = self.queue1[0]
        elif self.queue2:
            top = self.queue2[0]
        return top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.currentQueue == 0:
            if len(self.queue1) == 0:
                return True
            return False
        else:
            if len(self.queue2) == 0:
                return True
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()