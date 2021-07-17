from threading import Lock
class FooBar:
    def __init__(self, n):
        self.n = n
        self.lockFoo = Lock()
        self.lockBar = Lock()
        self.lockBar.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.lockFoo.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.lockBar.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.lockBar.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.lockFoo.release()