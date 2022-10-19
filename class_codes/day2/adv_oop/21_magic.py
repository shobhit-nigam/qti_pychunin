class CustomList:
    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        # if key is invaild , raise error
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def last(self):
        # get last item
        return self.values[-1]

    def half(self):
        half_length = len(self.values)//2
        return self.values[0:half_length]



objc = CustomList([11, 22, 33, 44, 55])
objd = CustomList()

print(objc[2])
objc[3] = "hello"
print(objc[3])
print(objc.half())
