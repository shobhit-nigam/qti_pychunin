class Sample:
    def __new__(cls, name):
        print("__new__nmagic metyhod is called")
        instance = object.__new__(cls)
        return instance

    def __init__(self, name):
        print("init is being called")
        self.name = name

hero = Sample("ironman")
