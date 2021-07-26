from threading import Lock
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.lockFizz = Lock()
        self.lockBuzz = Lock()
        self.lockFizzBuzz = Lock()
        self.lockNumber = Lock()
        self.lockFizz.acquire()
        self.lockBuzz.acquire()
        self.lockFizzBuzz.acquire()
        
    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
    	while True:
            self.lockFizz.acquire()
            if self.n == 0:
                break
            printFizz()
            self.lockNumber.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
    	while True:
            self.lockBuzz.acquire()
            if self.n == 0:
                break
            printBuzz()
            self.lockNumber.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.lockFizzBuzz.acquire()
            if self.n == 0:
                break
            printFizzBuzz()
            self.lockNumber.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,self.n+1):
            self.lockNumber.acquire()
            if i%15 == 0:
                self.lockFizzBuzz.release()
            elif i%3 == 0:
                self.lockFizz.release()
            elif i%5 == 0:
                self.lockBuzz.release()
            else:
                #print("sd",i)
                printNumber(i)
                self.lockNumber.release()
        self.lockNumber.acquire()
        self.n = 0
        self.lockFizz.release()
        self.lockBuzz.release()
        self.lockFizzBuzz.release()