class Sample:
    def __init__(self, varx):
        print("in init")
        self.varx = varx

    @property
    def varx(self):
        print("getting varx")
        return self.__varx

    @varx.setter
    def varx(self,val):
        print("setting varx")
        if val < 0:
            self.__varx=0
        elif val>200:
            self.varx=200
        else:
            self.__varx=val

# varx = property(get_varx, set_varx)

objp = Sample(40)
objq = Sample(70)

print(objp.varx)
objp.varx = 100
print(objp.varx)
