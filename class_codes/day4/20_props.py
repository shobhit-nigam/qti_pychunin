class Sample:
    def __init__(self, varx):
        self.varx = varx

    @property
    def get_varx(self):
        print("getting varx")
        return self.__varx

    @varx.setter
    def set_varx(self, val):
        print("setting varx")
        if val < 0:
            self.__varx = 0
        elif val > 200:
            self.varx = 200
        else:
            self.__varx = val


objp = Sample(40)
objq = Sample(70)

objp.set_varx(-100)
objq.set_varx(143)

print(objp.get_varx())
print(objq.get_varx())

potato = objp.varx
