from threading import Lock
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.lockZero = Lock()
        self.lockEven = Lock()
        self.lockOdd = Lock()
        self.lockEven.acquire()
        self.lockOdd.acquire()
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,self.n+1):
            self.lockZero.acquire()
            printNumber(0)
            if i%2 == 0:
                self.lockEven.release()
            else:
                self.lockOdd.release()
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,self.n+1):
            if i%2 == 0:
                self.lockEven.acquire()
                printNumber(i)
                self.lockZero.release()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,self.n+1):
            if i%2 == 1:
                self.lockOdd.acquire()
                printNumber(i)
                self.lockZero.release()
        