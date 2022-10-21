from abc import abstractmethod, ABC

class SampleA(ABC):
    def __init__(self, initval=None):
        print("init of a")
        self.val = initval

    def method_a(self):
        pass

    @abstractmethod
    def method_b(self):
        print("love indian food")
        pass

class SampleB(SampleA):
    pass

    def method_b(self):
        super().method_b()
        print("and also other cusines")


#obja = SampleA(99)
objb = SampleB(100)
objb.method_b()
