from abc import abstractmethod, ABC

class SampleA:
    def __init__(self, initval=None):
        print("init of a")
        self.val = initval

    def method_a(self):
        pass

    def method_b(self):
        pass

obja = SampleA(99)
