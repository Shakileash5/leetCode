from threading import Lock
class H2O:
    def __init__(self):
        self.hydrogenCount = 0
        self.hydrogenLock = Lock()
        self.oxygenLock = Lock()
        self.oxygenLock.acquire()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        self.hydrogenLock.acquire()
        releaseHydrogen()
        self.hydrogenCount += 1
        if self.hydrogenCount == 2:
            self.hydrogenCount = 0
            self.oxygenLock.release()
        else:
            self.hydrogenLock.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.oxygenLock.acquire()
        releaseOxygen()
        self.hydrogenLock.release()