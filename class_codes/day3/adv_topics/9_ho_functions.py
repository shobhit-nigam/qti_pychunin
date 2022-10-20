def bake(food):
    print(f"bake {food}")


def fry(food):
    print(f"fry {food}")

#bake("ccokies")
#fry("papad")

def cook(gen, food):
    gen(food)

cook(bake, 'cake')
