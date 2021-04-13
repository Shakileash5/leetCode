class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.currentStack = 0
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while(len(self.stack1)!=0):
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while(len(self.stack2)!=0):
            self.stack1.append(self.stack2.pop())
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        dequeued = None
        if len(self.stack1)!=0:
            dequeued = self.stack1.pop()
        return dequeued
        
    def peek(self) -> int:
        """
        Get the front element.
        """
        front = None
        if len(self.stack1)!=0:
            front = self.stack1[-1]
        return front
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.stack1)!=0:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()