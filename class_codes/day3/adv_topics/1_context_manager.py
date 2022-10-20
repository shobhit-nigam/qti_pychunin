with open("file.txt", "r") as objf:
    stra = objf.read()

print(f"stra = {stra}")
print(objf.closed)
