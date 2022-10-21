varx = 100
varb = ['aa', 'vv', 'rr', 'ii', 'ss']

def funcx():
    print("in func")
    la = 11
    lb = 22
    print(locals())
    print("-------")
    print(globals())

class Sample:
    data = 90

funcx()
