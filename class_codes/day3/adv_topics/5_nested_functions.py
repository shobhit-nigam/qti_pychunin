def funca():
    print("is a")

    def funcb():
        print("in b")
        return 100

    x = funcb()
    print("in a, ret val of b is", x)


funca()
