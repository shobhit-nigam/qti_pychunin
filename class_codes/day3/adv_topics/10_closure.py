
def funcb(gen):

    def funcc():
        print("some text")
    return funcc

funcx = funcb("may be froce be with you")

funcx()
