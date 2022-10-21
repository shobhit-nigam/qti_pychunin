class Sample:
    def __init__(self, varx):
        self.__varx = varx
    def get_varx(self):
        return self.__varx
    def set_varx(self, val):
        self.__varx = val

objp = Sample(40)
objq = Sample(70)
print(objp.get_varx())

objq.set_varx(objp.get_varx() + objq.get_varx())

print(objq.get_varx())
