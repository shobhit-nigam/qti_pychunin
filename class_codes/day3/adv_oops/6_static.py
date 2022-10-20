class Sample:
    data = 100
    info = 200

    def method_a(self, val):
        self.data = val

    @classmethod
    def method_b(cls, val):
        cls.data = val

    @staticmethod
    def method_c():
        pass

objx = Sample()
objy = Sample()

objx.method_c()
