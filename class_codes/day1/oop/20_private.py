class Sample:
    datap = 10
    _dataq = 200
    __datar = 300
    __datas__ = 400

    def display(self):
        print(f"datap = {self.datap}")
        print(f"_dataq = {self._dataq}")
        print(f"__datar = {self.__datar}")
        print(f"__datas__ = {self.__datas__}")

obja = Sample()

print(f"datap = {obja.datap}")
print(f"_dataq = {obja._dataq}")
#error
#print(f"__datar = {obja.__datar}")
print(f"__datas__ = {obja.__datas__}")
