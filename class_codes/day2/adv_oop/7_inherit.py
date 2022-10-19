class Parent:
    def __init__(self, x, y):
        self.varx = x
        self.vary = y

class Child(Parent):
    def __init__(self, x, y, z):
    #    super().__init__(x, y)
        Parent.__init__(self, x, y)
        self.varz = z

    def display(self):
        print(f"varx = {self.varx}")
        print(f"vary = {self.vary}")
        print(f"varz = {self.varz}")

objl = Child(88, 77, 66)
objl.display()
