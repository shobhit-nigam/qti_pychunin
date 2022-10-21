class Sample:
    def __init__(self, varx):
        self.__varx = varx

    def get_varx(self):
        return self.__varx

    def set_varx(self, val):
        if val < 0:
            self.__varx = 0
        elif val > 200:
            self.varx = 200
        else:
            self.__varx = val

    varx = property(get_varx, set_varx)

objp = Sample(40)
objq = Sample(70)

objp.set_varx(-100)
objq.set_varx(143)

print(objp.get_varx())
print(objq.get_varx())

#objp.varx = 650
