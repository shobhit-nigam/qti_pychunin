def funca():
    print("is a")

    def funcb():
        print("in b")

    print("in a")

funca()

#error
funca().funcb()
