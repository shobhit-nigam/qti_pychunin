def gen():
    n = 1
    print("first print")
    yield n

    n = n+n
    print("second print")
    yield n

    n = n+n
    print("final print")
    yield n

objg = gen()

print(next(objg))
print(next(objg))
print(next(objg))

# error
print(next(objg))
