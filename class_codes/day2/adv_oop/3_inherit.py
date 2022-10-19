class Unix:
    max_files = 50
    def cmd(self):
        print("great command line")

    def secure(self):
        print("rwx makes it safer")

class Linux(Unix):
    max_files = 120
    def free(self):
        print("opensource and free")

    def open_files(self):
        print(f"maximum files that can be opened in user mode is {self.max_files}")
        print(f"maximum files that can be opened in privileged mode is {super().max_files}")

obju = Unix()
objl = Linux()

objl.open_files()
