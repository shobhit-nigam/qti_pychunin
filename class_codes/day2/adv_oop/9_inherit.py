class Unix:
    def cmd(self):
        print("great command line")

    def secure(self):
        print("rwx makes it safer")

class Linux(Unix):
    def free(self):
        print("opensource and free")

    def portable(self):
        print("portable to many devices")

class mobileOS:
    def ui(self):
        print("great UI")

    def portable(self):
        print("portable to hand held devices")

class Android(mobileOS, Linux ):
    def APIs(self):
        print("rich set of APIs")

obju = Unix()
objl = Linux()
obja = Android()

obja.portable()
