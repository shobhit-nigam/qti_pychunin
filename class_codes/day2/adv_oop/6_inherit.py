class Unix:

    def __init__(self):
        print("init of unix")

    def cmd(self):
        print("great CLI, plain black&white")

    def secure(self):
        print("rwx makes it safer")

class Linux(Unix):

    def __init__(self):
        print("init of linux")

    def free(self):
        print("opensource and free")


#obju = Unix()
objl = Linux()

objl.cmd()
