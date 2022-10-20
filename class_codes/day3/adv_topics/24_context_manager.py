
from contextlib import contextmanager

@contextmanager
def funca():
    print("enter method")
    yield

    print("exit method")

with funca() as objm:
    print("with statement block")
