from abc import abstractmethod, ABC

class SampleA(ABC):
    def __init__(self, initval=None):
        print("init of a")
        self.val = initval

    def method_a(self):
        pass

    @abstractmethod
    def method_b(self):
        pass

class SampleB(SampleA):
    pass

    def method_b(self):
        return self.val - 20


#obja = SampleA(99)
objb = SampleB(100)
