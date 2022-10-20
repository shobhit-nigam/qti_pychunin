import time
listx = [11, 22, 33, 44]

obji = iter(listx)

while True:
    try:
        varx = next(obji)
        print(varx)
        time.sleep(3)

    except StopIteration:
        print("will exit now")
        time.sleep(1)
        break;
