class Sample:
    data = 100
    info = 200

    def method_a(self, val):
        self.data = val

objx = Sample()
objy = Sample()
objx.data = 50
print(f"Sample.data = {Sample.data}")
print(f"objx.data = {objx.data}")
print(f"objy.data = {objy.data}")
Sample.data = 99
print(f"Sample.data = {Sample.data}")
print(f"objx.data = {objx.data}")
print(f"objy.data = {objy.data}")
