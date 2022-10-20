def funca():
    varx = 10
    print(f"outside varx = {varx}")

    def funcb():
        nonlocal varx
        varx = 100
        print(f"inside varx = {varx}")
    x = funcb()
    print(f"outside varx = {varx}")


funca()
