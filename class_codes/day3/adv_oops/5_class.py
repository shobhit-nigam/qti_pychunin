class Sample:
    data = 100
    info = 200

    def method_a(self, val):
        self.data = val

    @classmethod
    def method_b(cls, val):
        cls.data = val


objx = Sample()
objy = Sample()
objx.method_a(50)
print(f"Sample.data = {Sample.data}")
print(f"objx.data = {objx.data}")
print(f"objy.data = {objy.data}")
objx.method_b(66)
print(f"Sample.data = {Sample.data}")
print(f"objx.data = {objx.data}")
print(f"objy.data = {objy.data}")

objz = Sample()
print(f"Sample.data = {Sample.data}")
print(f"objz.data = {objz.data}")
print(f"objy.data = {objy.data}")
