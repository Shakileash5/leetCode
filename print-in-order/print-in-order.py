class Foo:
    def __init__(self):
        self.flagOne = False
        self.flagTwo = False


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        while self.flagOne == True:
            continue
        printFirst()
        self.flagOne = True


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        while self.flagOne == False:
            continue
        printSecond()
        self.flagTwo = True


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        while self.flagTwo == False:
            continue
        printThird()