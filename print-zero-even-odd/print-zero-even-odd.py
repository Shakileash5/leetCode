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
        for i in range(self.n): 
            self.lockZero.acquire()
            printNumber(0)
            if i%2 == 0:
                self.lockOdd.release()
            else:
                self.lockEven.release()
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2,self.n+1,2):
            self.lockEven.acquire()
            printNumber(i)
            self.lockZero.release()
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,self.n+1,2):
            self.lockOdd.acquire()
            printNumber(i)
            self.lockZero.release()
        